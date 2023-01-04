class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternDict = defaultdict(list)
        wordDict = defaultdict(list)
        
        words= s.split(' ')

        if len(pattern) != len(words): 
            return False
        
        if len(set(pattern)) != len(set(words)): 
            return False

        for index, char in enumerate(pattern):
            patternDict[char].append(index)
        
        for index, word in enumerate(words):
            wordDict[word].append(index)
        
        for a, b in zip(patternDict.values(), wordDict.values()):
            if a != b:
                return False
        return True
