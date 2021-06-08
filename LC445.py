# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 弄成list，因为要倒序
        ls1, ls2 = [], []
        while l1: 
            ls1.append(l1.val)
            l1 = l1.next
        while l2:
            ls2.append(l2.val)
            l2 = l2.next
        
        # reverse
        ls1, ls2 = ls1[::-1], ls2[::-1]
        
        # 短的补零
        if len(ls1)>len(ls2):
            lsT = [0]*len(ls1)
            for i in range(len(ls2)):
                lsT[i] = ls2[i]
            ls2 = lsT
        elif len(ls2)>len(ls1):
            lsT = [0]*len(ls2)
            for i in range(len(ls1)):
                lsT[i] = ls1[i] 
            ls1 = lsT
        
        acc = 0 # 进位
        res = []
        while ls1 and ls2:
            temp = ls1[0]+ls2[0]+acc
            if  temp > 9:
                acc = 1
                res.append(temp%10)
            else:
                res.append(temp)
                acc = 0
            ls1.pop(0)
            ls2.pop(0)
        
        if acc == 1:
            res.append(1)
        
        # make linked list
        res = res[::-1]
        head = ListNode()
        cur = head
        for it in res:
            cur.next = ListNode(it)
            cur = cur.next
        head = head.next
        return head
            