class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictionary = {}
        
        # for every char in string s
        for index, char in enumerate(s):
            
            # if char doesn't exist in dictionary
            # check if char at index in string t exists in dictionary values
            # if yes, return false, else assign char at index in t to char
            # if char exists in dictionary and char at index in t != dictionary[char]
            # return false
            
            if char not in dictionary:
                if t[index] in dictionary.values():
                    return False
                else:
                    dictionary[char] = t[index]
                    
            else:
                if dictionary[char] != t[index]:
                    return False
                
        return True