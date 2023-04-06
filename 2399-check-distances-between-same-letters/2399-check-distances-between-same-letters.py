class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        unique = set(s)
        for char in unique:
            index = s.index(char) # get the first index of the char
            dis = distance[ord(char) - 97]
            if index + dis + 1 > len(s) - 1 or s[index + dis + 1] != char:
                return False
        return True