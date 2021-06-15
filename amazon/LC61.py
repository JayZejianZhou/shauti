# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # get the length of the list
        head_cp = head
        length = 0
        while head:
            length += 1
            if not head.next: last = head
            head = head.next
            
                
                
        if length <= 1 or k == 0: return head_cp
        
        k = length - k%length
        
        if k==length: return head_cp
        
        # find the rotated start
        start = head_cp
        while k>0: 
            start = start.next
            k -= 1
            
        # make a circle and rotate
        start_cp = start
        last.next = head_cp
        while length>1:
            start = start.next
            length -= 1
        
        start.next = None
        
        return start_cp