class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        
        for word in words:
            if set(word) <= allowed:
                count += 1
        return count