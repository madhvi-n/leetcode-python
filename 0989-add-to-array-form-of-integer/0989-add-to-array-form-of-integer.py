class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        curr = 0
        
        for char in num:
            curr = 10 * curr + char
        curr = curr + k
        
        return [int(char) for char in str(curr)]