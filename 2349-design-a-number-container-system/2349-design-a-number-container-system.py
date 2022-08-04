class NumberContainers:

    def __init__(self):
        # index mapping to num maintain updated version of cur container
        self.indexNum = {} 
        # number: a heap storing a history of indexes that this number has been stored to
        self.numbersHeap = defaultdict(list) 
        # number: a set keeping track of the current version of indexes that this number is stored at 
        self.numberIndexes = defaultdict(set) 
        
    def change(self, index: int, number: int) -> None:
        # if the index has been used, look up what number it stored, and kick off the index from the current index set of that number
        if index in self.indexNum:
            origin = self.indexNum[index]
            self.numberIndexes[origin].remove(index)
        # update the storages
        self.indexNum[index] = number
        heappush(self.numbersHeap[number], index)
        self.numberIndexes[number].add(index)
            
    def find(self, number: int) -> int:
        # heap[0] maintains the smallest index the number has been stored in the history. Check the set to make sure it still be smallest at current moment. If not, we discard it.
        while self.numbersHeap[number] and \
        self.numbersHeap[number][0] not in self.numberIndexes[number]:
            heappop(self.numbersHeap[number])
        return self.numbersHeap[number][0] if self.numbersHeap[number] else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)