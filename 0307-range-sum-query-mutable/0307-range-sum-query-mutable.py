class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None
        
class NumArray:
    
    def __init__(self, nums: List[int]):
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            root.sum = nums[start]
        else:
            mid = (start + end) // 2
            root.left = self.build_tree(nums, start, mid)
            root.right = self.build_tree(nums, mid + 1, end)
            root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root, index, val):
        if root.start == root.end:
            root.sum = val
        else:
            mid = (root.start + root.end) // 2
            if index <= mid:
                self.update_helper(root.left, index, val)
            else:
                self.update_helper(root.right, index, val)
            root.sum = root.left.sum + root.right.sum

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRange_helper(self.root, left, right)

    def sumRange_helper(self, root, left, right):
        if root.start == left and root.end == right:
            return root.sum
        mid = (root.start + root.end) // 2
        if right <= mid:
            return self.sumRange_helper(root.left, left, right)
        elif left > mid:
            return self.sumRange_helper(root.right, left, right)
        else:
            return self.sumRange_helper(root.left, left, mid) + \
                   self.sumRange_helper(root.right, mid + 1, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)