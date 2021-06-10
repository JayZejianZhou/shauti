# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        sameVal = []    # 存放找到的相等数值
        self.find(root, subRoot, sameVal)        
        if not sameVal: return False   # 找不到
        res = [] 
        for it in sameVal:
            resO, resR = [], []
            self.traverse(it, resO)
            self.traverse(subRoot, resR)
            if resO==resR: return True
        return False
        
    # 遍历这棵树
    def traverse(self, base, res):   
        if not base: 
            res.append(None)
            return 0
        res.append(base.val)
        
        self.traverse(base.left, res)
        self.traverse(base.right, res)
    
    # 找到一个点
    def find(self, base, tar, sameVal):
        if not base: return -1
        if base.val==tar.val: sameVal.append(base)       
        self.find(base.left, tar, sameVal)
        self.find(base.right, tar, sameVal)
        