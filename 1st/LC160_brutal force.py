# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        bNext = headB
        while bNext:
            cur = self.helper(headA, bNext)
            if cur:
                return cur
            bNext = bNext.next
        return None
        
    def helper(self, headA, headB):
        aNext = headA
        while aNext:
            if aNext == headB:
                return aNext
            else:
                aNext = aNext.next
        return None
            
        