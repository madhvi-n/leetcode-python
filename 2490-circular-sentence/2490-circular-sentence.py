class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if len(sentence) == 1 and sentence[0] == sentence[-1]:
            return True
        
        sentence = sentence.split()
        
        for i in range(len(sentence)):
            curr = sentence[i]
            nxt = sentence[i + 1] if (i + 1) < len(sentence) else sentence[0]
            
            if curr[-1] != nxt[0]:
                return False
        
        return True