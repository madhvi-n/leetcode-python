class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        values = dict()
        for index, num in enumerate(sorted(nums)):
            if num not in values:
                values[num] = index
        return [values[num] for num in nums]