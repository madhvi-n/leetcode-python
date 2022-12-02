class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
#         pcount, qcount = 0, 0
        
#         for i in range(half):
#             p, q = s[i], s[half + i]
            
#             if p in vowels:
#                 pcount += 1
                
#             if q in vowels:
#                 qcount += 1
                
#         return pcount == qcount
        n = len(s)
        return sum(i in vowels for i in s[:n//2]) == sum(i in vowels for i in s[n//2:])