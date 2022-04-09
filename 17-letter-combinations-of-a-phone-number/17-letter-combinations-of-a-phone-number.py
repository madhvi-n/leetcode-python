class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        length = len(digits)
        res = []
        
        if (length == 0):
            return res
        
        def backtrack(index, candidate, digits, res):
            if (index == len(digits)):
                res.append(candidate)
                return
                
            for next_char in mapping[digits[index]]:
                candidate += next_char
                backtrack(index + 1, candidate, digits, res)
                candidate = candidate[0:-1]
        
        backtrack(0, "", digits, res)
        
        return res