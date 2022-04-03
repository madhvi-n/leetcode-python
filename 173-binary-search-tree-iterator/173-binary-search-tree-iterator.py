# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.elements = self.inorder(root)
        self.pointer = 0
        
    def inorder(self, root):
        elements = []
        if root.left:
            elements += self.inorder(root.left)
        
        elements.append(root.val)
        
        if root.right:
            elements += self.inorder(root.right)
            
        return elements
    
    def next(self) -> int:
        if self.hasNext:
            el = self.elements[self.pointer]
            self.pointer += 1
            return el
    
    def hasNext(self) -> bool:
        return self.pointer < len(self.elements)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()