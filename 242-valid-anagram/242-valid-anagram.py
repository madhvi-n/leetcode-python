class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMap = dict()

        #Add count of characters into hashMap for one string and remove count for another
        #If count is greater than 0 for any string, not an anagram
        
        for character in s:
            hashMap[character] = 1 + hashMap.get(character, 0)

        for character in t:
            if character in hashMap:
                hashMap[character] -= 1

        for count in hashMap.values():
            if count > 0:
                return False
        return True
            
        
