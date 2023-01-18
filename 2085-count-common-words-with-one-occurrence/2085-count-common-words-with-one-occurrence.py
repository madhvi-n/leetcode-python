class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counts1 = Counter(words1)
        counts2 = Counter(words2)
        return sum(counts1[key] == counts2[key] == 1 for key in counts1)
