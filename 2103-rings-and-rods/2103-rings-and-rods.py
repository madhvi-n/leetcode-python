class Solution:
    def countPoints(self, rings: str) -> int:
        hashmap = defaultdict(set)
        
        for i in range(0, len(rings), 2):
            color, index = rings[i:i+2]
            hashmap[index].add(color)
        
        count = 0  
        for index, values in hashmap.items():
            if len(values) == 3:
                count += 1
        return count