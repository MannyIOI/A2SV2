# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        curr, mid = head, head
        i = 0
        while curr:
            if curr.next is None:
                return mid
            
            if i % 2 == 0:
                mid = mid.next
            
            curr = curr.next
            i = i + 1
            
        return mid