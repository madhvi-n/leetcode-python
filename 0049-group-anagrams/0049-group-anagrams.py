class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            hashmap[key].append(word)
        return hashmap.values()