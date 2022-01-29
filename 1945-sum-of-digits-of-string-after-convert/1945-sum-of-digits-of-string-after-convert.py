class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ''
        
        for char in s:
            nums += str(ord(char) - ord('a') + 1)
        
        for i in range(k):
            nums = str(sum((int(c) for c in nums)))

        return nums