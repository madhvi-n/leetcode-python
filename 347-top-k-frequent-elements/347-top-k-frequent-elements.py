class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        res = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        
        result = []
        
        for x in res.keys():
            result.append(x)
            k -= 1
            if k == 0:
                break
        return result