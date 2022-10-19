class Solution:
    def equalFrequency(self, word: str) -> bool:
        mapping = Counter(word)
        counter = Counter(mapping.values())
        
        keys, values = counter.keys(), counter.values()
        
        if len(counter) == 1:
            return 1 in keys or 1 in values
        
        if len(counter) == 2:
            f1, f2 = min(keys), max(keys)
            return (f1 + 1 == f2 and counter[f2] == 1) or (f1 == 1 and counter[f1] == 1)
        return False