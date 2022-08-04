# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        p, prev, count, nums = head, False, 0, set(nums)
        while p:
            if p.val in nums and not prev:
                count += 1
            prev, p = p.val in nums, p.next;
        
        return count