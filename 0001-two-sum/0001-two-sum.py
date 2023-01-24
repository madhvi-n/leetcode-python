class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [index, hashmap.get(diff)]            
            hashmap[num] = index
