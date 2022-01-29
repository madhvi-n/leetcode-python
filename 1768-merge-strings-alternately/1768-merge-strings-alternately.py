class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        
        for x, y in zip(word1, word2):
            result += x
            result += y
        
        #In case strings aren't of equal length
        if len(word1) != len(word2):
            # find string of max length
            maxstr = word1
            if len(word2) > len(word1):
                maxstr = word2
            
            #find the remaining string that needs to be joined using result string
            result += maxstr[len(result)//2:]
            
        return result