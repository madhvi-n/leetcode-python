class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: 0}
        
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            
            if total % k not in hashmap:
                hashmap[total % k] = i + 1
            
            elif hashmap[total % k] < i:
                return True
            
        return False