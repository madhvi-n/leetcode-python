import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hashmap = {}
        
#         for num in nums:
#             hashmap[num] = 1 + hashmap.get(num, 0)
        
#         res = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        
#         result = []
        
#         for x in res.keys():
#             result.append(x)
#             k -= 1
#             if k == 0:
#                 break
#         return result

        count = dict()
        frequency = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        for n, c in count.items():
            frequency[c].append(n)
        
        res = []
        
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
