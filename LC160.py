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
        # save a few nodes
        # calculate the node number of the two linked list
        pa, pb = headA, headB
        numa, numb = 0, 0
        while pa:
            numa += 1
            pa = pa.next
        while pb:
            numb += 1
            pb = pb.next
        # eliminate the a few nodes
        if numb > numa:
            for i in range(numb - numa):
                headB = headB.next
        elif numa > numb:
            for i in range(numa - numb):
                headA = headA.next    
                
       # then we only need to move the pointer for both linked lists at the same time
        pa, pb = headA, headB
        while pa and pb:
            if pa==pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None