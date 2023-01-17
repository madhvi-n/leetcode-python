class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        curr = 0
        
        for char in num:
            curr = 10 * curr + char
        curr = curr + k
        
        res = []
        
        for char in str(curr):
            res.append(int(char))
        
        return res