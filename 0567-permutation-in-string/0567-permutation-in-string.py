class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(list(s1)))
        
        for i in range(len(s2)):
            if s1 == "".join(sorted(list(s2[i:i+len(s1)]))):
                return True
        return False