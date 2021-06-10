# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        used = []
        cur = head
        
        if not head:
            return False
        
        while cur.next:
            used.append(cur)
            cur = cur.next
            if cur in used:
                return True
            
        return False