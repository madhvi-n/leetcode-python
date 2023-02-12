class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = dict()
        
        for char in s:
            hashmap[char] = 1 + hashmap.get(char, 0)
            
        freq = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        
        res = ""
        for key, val in freq.items():
            res += key * val
        return res