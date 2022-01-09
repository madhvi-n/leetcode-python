class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int: 
        wealth = [sum(nums) for i, nums in enumerate(accounts)]
        return max(wealth)