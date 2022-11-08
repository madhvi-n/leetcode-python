class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        first_row = set("qwertyuiopQWERTYUIOP")
        second_row = set("asdfghjklASDFGHJKL")
        third_row = set("zxcvbnmZXCVBNM")
        
        for word in words:
            curr = set(word)
            if curr.issubset(first_row) or \
                curr.issubset(second_row) or \
                curr.issubset(third_row):
                    res.append(word)
        return res