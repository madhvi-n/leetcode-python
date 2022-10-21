class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        
        for index, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [hashmap.get(difference),index]
            hashmap[num] = index
        return [-1, -1]