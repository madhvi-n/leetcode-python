class Solution:
    def reverseVowels(self, s: str) -> str:
        inStringVowels = [] #vowels in input string
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] #list of vowels
        
        lst = list(s)
        
        for i in range(len(lst)):
            if lst[i] in vowels:
                inStringVowels.append(lst[i])
                lst[i] = '_'
        
        for i in range(len(lst)):
            if lst[i] == '_':
                lst[i] = inStringVowels.pop()
                
        return "".join(lst)
