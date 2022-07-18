class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            # i is the position and nums[i] are the steps to reach the goal
            # if curr position and no of steps are enough to reach the goal, shift goal to i
            if i + nums[i] >= goal:
                goal = i
            
        return True if goal == 0 else False