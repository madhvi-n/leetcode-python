class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        k = word.find(ch)
        prefix = word[:(k+1)]
        return prefix[::-1] + word[k+1:]