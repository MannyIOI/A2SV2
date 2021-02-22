# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # reverse = self.reverseList(head)
        
        curr = head
        count = 0
        while curr != None:
            curr = curr.next
            count += 1
        
        curr = head
        for i in range(count // 2):
            curr = curr.next
        
        
        reverse = self.reverseList(curr)
        curr = head
        
        for i in range(count // 2):
            if curr.val != reverse.val:
                return False
            
            curr = curr.next
            reverse = reverse.next
    
        return True
        
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