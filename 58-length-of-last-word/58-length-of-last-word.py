class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        lst.reverse()
        return len(lst[0])