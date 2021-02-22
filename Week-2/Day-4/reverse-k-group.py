# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        curr = head
        idx = 1
        new_head = head
        tmp_head = None
        last_tail = None
        while curr != None:
            next_node = curr.next
            # if modulo one it's the first element and it's going to be the last element
            if idx % k == 1:
                tmp_head = curr
            
            if idx == k:
                new_head = curr

            # if modulo 0 it's the last element and it's going to be the first element
            if idx % k == 0:
                new_tail = tmp_head
                curr.next = None
                curr = self.reverseList(tmp_head)
                
                if last_tail:
                    last_tail.next = curr 
                
                last_tail = tmp_head
                
            curr = next_node
            idx += 1
        
        if last_tail and (idx - 1) % k != 0:
            last_tail.next = tmp_head
        
        return new_head

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            next = curr.next

            curr.next = prev

            prev = curr
            if next == None:
                break
            curr = next

        return curr