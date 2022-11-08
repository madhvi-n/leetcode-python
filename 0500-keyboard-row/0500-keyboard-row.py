class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        first_row = "qwertyuiopQWERTYUIOP"
        second_row = "asdfghjklASDFGHJKL"
        third_row = "zxcvbnmZXCVBNM"
        
        for word in words:
            if set(word).issubset(set(first_row)) or \
                set(word).issubset(set(second_row)) or \
                set(word).issubset(set(third_row)):
                    res.append(word)
        return res