class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        array = [int(c) for c in s.split() if c.isdigit()]
        
        for i in range(len(array) - 1):
            if array[i] > array[i+ 1] or array[i] == array[i+1]:
                return False
        return True
        
        