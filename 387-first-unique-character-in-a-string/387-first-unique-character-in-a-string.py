class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = dict()
        
        for char in s:
            hashmap[char] = 1 + hashmap.get(char, 0)
        
        for index, char in enumerate(s):
            if hashmap[char] == 1:
                return index
        return -1
        
    