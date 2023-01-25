class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
#         if len(sentence) == 1 and sentence[0] == sentence[-1]:
#             return True
        
        sentence = sentence.split()
        
        # for each word, check next word
        # if current's last is not equal to next's first character, return False
        
        for i in range(len(sentence)):
            curr = sentence[i - 1]
            nxt = sentence[i]
            
            if curr[-1] != nxt[0]:
                return False
        
        return True