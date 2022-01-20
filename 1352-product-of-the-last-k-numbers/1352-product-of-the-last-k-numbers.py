class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.zero_index = -1
    

    
    
    def add(self, num: int) -> None:
        if num != 0 and len(self.arr) > 0:
            last_number = self.arr[-1]
            self.arr.append(last_number*num if last_number!=0 else num)        
        else:
            if len(self.arr) > 0 or num == 0:
                self.zero_index = len(self.arr)
            self.arr.append(num)
            
    def getProduct(self, k: int) -> int:
        length = len(self.arr)
        index = length - k -1
        
        if index >self.zero_index:
            return self.arr[-1] // self.arr[index]
        
        if index == self.zero_index:
            return self.arr[-1]
        return 0