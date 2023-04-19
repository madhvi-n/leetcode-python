class Solution:
    def sortString(self, s: str) -> str:
        freq = Counter(s)
        res = ""
        string = "abcdefghijklmnopqrstuvwxyz"
        
        while True:
            for char in string:
                if char in freq:
                    freq[char] -= 1
                    res += char

                    if freq[char] == 0:
                        freq.pop(char)

            for char in string[::-1]:
                if char in freq:
                    freq[char] -= 1
                    res += char
                    
                    if freq[char] == 0:
                        freq.pop(char)
            
            if not freq:
                break
                
        return res