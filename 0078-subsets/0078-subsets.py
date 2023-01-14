class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def backtrack(start, cur_list):
            ans.append(cur_list[:])

            for j in range(start, n):
                cur_list.append(nums[j])
                backtrack(j+1, cur_list)
                cur_list.pop()

        backtrack(0, [])
        return ans