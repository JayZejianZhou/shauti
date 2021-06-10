# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cur_max = float('-inf')
        res = self.helper(root.left) + self.helper(root.right)
        
        
        
        return max(res, self.cur_max)
        
        
    # 注意，可能是在中间左右子树之和就是最大了
    def helper(self, base):
        if not base:
            return 0

        left_val = self.helper(base.left)
        right_val = self.helper(base.right)
        combine =  max(left_val, right_val) + 1
        
        self.cur_max = max(self.cur_max, left_val+right_val)

        return combine