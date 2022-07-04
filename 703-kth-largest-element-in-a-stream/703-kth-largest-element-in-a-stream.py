class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stack = nums
        self.k = k

    def add(self, val: int) -> int:
        self.stack.append(val)
        self.stack.sort()
        return self.stack[len(self.stack)-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

