class Solution:
    def equalFrequency(self, word: str) -> bool:
#         counter = Counter(Counter(word))
#         keys, values = counter.keys(), counter.values()

#         if len(counter) == 1:
#             return 1 in keys or 1 in values
        
#         if len(counter) == 2:
#             f1, f2 = min(keys), max(keys)
#             return (f1 + 1 == f2 and counter[f2] == 1) or (f1 == 1 and counter[f1] == 1)
#         return False
    
        cnt = Counter(Counter(word).values())
        if (len(cnt) == 1):
            return 1 in cnt.keys() or 1 in cnt.values()
        if (len(cnt) == 2):
            f1, f2 = min(cnt.keys()), max(cnt.keys())
            return (f1 + 1 == f2 and cnt[f2] == 1) or (f1 == 1 and cnt[f1] == 1)
        return False