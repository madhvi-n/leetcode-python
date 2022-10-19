class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
#         seen = [False] * 26
        
#         for curr_char in sentence:
#             seen[ord(curr_char) - ord('a')] = True
        
#         for status in seen:
#             if not status:
#                 return False
#         return True

        counter = set(sentence)
        return len(counter) == 26
        
        