class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(num) for num in digits]))        
        return [int(i) for i in str(num + 1)]

    