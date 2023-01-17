class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ''.join(char if char.isdigit() else ' ' for char in word)
        return len(set(map(int, s.split())))