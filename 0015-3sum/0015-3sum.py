class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seen = set()
        nums.sort()
        
        for index, a in enumerate(nums):
            if a in seen:
                continue
            seen.add(a)

            left, right = index + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.add((a, nums[left], nums[right]))
                    left += 1
        return list(res)