class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
#         hashmap = defaultdict(list)
        
#         for i in range(len(nums) - 1):
#             hashmap[(nums[i] + nums[i+1])].append((nums[i], nums[i+1]))
        
#         for subarraySum, values in hashmap.items():
#             if len(values) >= 2:
#                 return True
#         return False

        subarraySum = set()
        for i in range(len(nums) - 1):
            currSum = nums[i] + nums[i+1]
            if currSum in subarraySum:
                return True
            subarraySum.add(currSum)
        return False