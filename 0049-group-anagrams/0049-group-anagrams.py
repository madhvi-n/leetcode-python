class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
#         counter = defaultdict(list)
#         for word in words:
#             w = "".join(sorted(word))
#             counter[w] += [word]

#         result = []
#         for values in counter.values():
#             result.append(values)
#         return result
    
        hashmap = defaultdict(list)
        for word in words:
            hashmap[tuple(sorted(word))].append(word)
        return list(hashmap.values())