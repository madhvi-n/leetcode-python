class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        order = defaultdict(list)
        
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                order[r + c].append(nums[r][c])
        
        res = []
        for val in order.values():
            res.extend(val[::-1])
        return res