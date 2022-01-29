class Solution:
    def reverseWords(self, s: str) -> str:
        string = " ".join(word[::-1] for word in s.split())
        return string
