# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        
        answer = [0] * len(arr)
        
        for i, val in enumerate(arr):
            while stack and arr[stack[-1]] < val:
                answer[stack.pop()] = val
            stack.append(i)
        
        return answer