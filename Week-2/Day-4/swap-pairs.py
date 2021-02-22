# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        idx = 0
        curr = head
        while curr != None:
            if idx % 2 == 0 and curr.next != None:
                curr.val, curr.next.val = curr.next.val, curr.val
            
            curr = curr.next
            idx += 1
        return head
            