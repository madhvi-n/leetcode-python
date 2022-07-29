class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            p = {}
            for x, y in zip(pattern, word):
                if p.setdefault(x, y) != y:
                    return False
            return len(set(p.values())) == len(p.values())
        
        result = []
        for word in words:
            if match(word):
                result.append(word)
        return result