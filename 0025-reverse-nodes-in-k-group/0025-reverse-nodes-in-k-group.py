# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, curr = 0, head
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k: 
            return head   # list shorter than k
        
        new_head, prev = self.reverseList(head, k)
        head.next = self.reverseKGroup(new_head, k)   
        # the size-k reversed list produced by sefl.reverseList(head, k) reads: prev -> ... -> head
        return prev

    def reverseList(self, head: ListNode, count: int) -> ListNode:
        prev = ListNode(None)
        curr = head
        while count > 0:
            next_node = curr.next   # break curr -> curr.next
            curr.next = prev   # reverse to prev <- curr
            prev = curr   # increment prev node
            curr = next_node   # increment curr node
            count -= 1
        return (curr, prev)   
        # prev is the head node of the reversed list, the end node of the original list
        # curr is the head node of the remaining list, since it is the node following prev in the original list