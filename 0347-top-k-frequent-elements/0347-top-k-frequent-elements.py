import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = dict()
#         frequency = defaultdict(list)
        
#         for num in nums:
#             count[num] = 1 + count.get(num, 0)
            
#         for n, c in count.items():
#             frequency[c].append(n)
        
#         res = []
        
#         for i in range(len(frequency) - 1, 0, -1):
#             for n in frequency[i]:
#                 res.append(n)
                
#                 if len(res) == k:
#                     return res
        
#         if len(nums) == 1:
#             return [nums[0]]

        # freq dict
        d = defaultdict(int)
        
        for num in nums:
            d[num] += 1

        # insert k items into heap O(nlog(k))
        h = []
        from heapq import heappush, heappop
        for key in d: # O(N)
            heappush(h, (d[key], key)) # freq, item - O(log(k))
            if len(h) > k:
                heappop(h)

        res = []
        while h: # O(k)
            frq, item = heappop(h) # O(logk)
            res.append(item)
        return res
