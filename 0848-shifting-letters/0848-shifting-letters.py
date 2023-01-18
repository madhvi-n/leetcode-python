class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = []
        X = sum(shifts) % 26
        
        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            ans.append(chr(ord('a') + (index + X) % 26))
            X = (X - shifts[i]) % 26

        return "".join(ans)