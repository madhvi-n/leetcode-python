class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter_one = dict(Counter(word1))
        counter_two = dict(Counter(word2))
        
        if len(counter_one.keys()) != len(counter_two.keys()):
            return False
        
        return set(counter_one.keys()) == set(counter_two.keys()) and sorted(counter_one.values()) == sorted(counter_two.values())