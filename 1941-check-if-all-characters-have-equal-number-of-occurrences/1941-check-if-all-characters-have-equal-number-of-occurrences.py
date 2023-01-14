class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = dict()
        
        for char in s:
            hashmap[char] = 1 + hashmap.get(char, 0)
        
        min_val = min(hashmap.values())
        max_val = max(hashmap.values())
        
        return min_val == max_val