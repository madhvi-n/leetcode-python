class Solution:
    def intToRoman(self, num: int) -> str:
        symbols= [
            ['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10],
            ['XL', 40], ['L', 50], ['XC', 90], ['C', 100],
            ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]
        ]
        
        result = ""
        for symbol, val in reversed(symbols):
            if num // val:
                # store the count of symbols and update it to result
                count = num // val
                result += (symbol * count)
                
                # update the num after integer division
                num = num % val
        return result