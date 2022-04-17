class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        
        print(nums)
        stack = []
        count = 0
        
        for num in nums:
            if stack:
                if num > stack[-1] and num - stack[-1] == 1:
                    stack.append(num)
                else:
                    count = max(count, len(stack))
                    stack = []
                    stack.append(num)
            else:
                stack.append(num)
            count = max(count, len(stack))
        return count