class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = "".join(word for word in word1)
        str2 = "".join(word for word in word2)
        
        return str1 == str2