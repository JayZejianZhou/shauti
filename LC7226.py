# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return root
        
        self.helper(root)
        
        return root
        
        
    def helper(self, base):
        if not base:
            return 0
        base.left, base.right = base.right, base.left
        self.helper(base.left)
        self.helper(base.right)