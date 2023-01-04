class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        # best case
        if len(nums) == 1:
            return nums[0]

        # apply the algorithm till my list has length 1
        while len(nums) != 1:
            # calculate current num value and append it to modified array
            modified_array = []
            for i in range(0, len(nums) // 2):
                curr_num = -1
                if i % 2 == 0:
                    curr_num = min(nums[2 * i], nums[2 * i + 1])
                else:
                    curr_num = max(nums[2 * i], nums[2 * i + 1])
                modified_array.append(curr_num)

            # replace the original with modified array
            nums = modified_array
        return nums[0]