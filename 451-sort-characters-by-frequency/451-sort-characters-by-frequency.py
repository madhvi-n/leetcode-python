class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        
        for char in s:
            hashmap[char] = 1 + hashmap.get(char, 0)
        
        res = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        
        string = ""
        
        for key, val in res.items():
            string += key * val
        
        return string