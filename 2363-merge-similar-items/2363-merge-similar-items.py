class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        hashmap = defaultdict(int)
        
        for value, weight in items1:
            hashmap[value] += weight
        
        for value, weight in items2:
            hashmap[value] += weight
        
        return sorted(hashmap.items())