class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = int(num / 3)
        
        if sum([x - 1, x, x + 1]) == num:
            return [x-1, x, x+1]
        else:
            return []