# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        
        return self.mergeTwoLists(lists[0], self.mergeKLists(lists[1:]))
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()

        curr = head
        while l1 != None or l2 != None:
            
            if l1 == None and l2 != None:
                curr.next = l2
                curr = curr.next
                break
            if l2 == None and l1 != None:
                curr.next = l1
                curr = curr.next
                break
            
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            

            curr = curr.next
            
        return head.next