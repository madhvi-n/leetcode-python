class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substring = set()
        
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] != words[j] and words[j] in words[i]:
                    substring.add(words[j])
        
        return substring