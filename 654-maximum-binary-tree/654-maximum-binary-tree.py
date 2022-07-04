# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def maxTree(nums):
            index = nums.index(max(nums))
            
            node = TreeNode(nums[index])
            
            if nums[index+1:]:
                node.right = maxTree(nums[index + 1:])

            if nums[:index]:
                node.left = maxTree(nums[:index])
                
            return node
        return maxTree(nums)
            
            