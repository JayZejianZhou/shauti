# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        condL, condR = True, True
        if root.left: condL = self.helper(root.left, root.val, float("-inf"))
        if root.right: condR = self.helper(root.right, float("inf"), root.val)
        return  condL and condR
    
    # maxx: max root, minn, min root, pos:"L" or "R"
    def helper(self, base, maxx, minn):
        if not base: return True
        elif base.val >= maxx or base.val <= minn: return False
        condL, condR = True, True
        # 区间[minn, maxx]
        if base.left: condL = self.helper(base.left, maxx = base.val, minn = minn) # 我的左子树一定要比我自己小
        if base.right: condR = self.helper(base.right, maxx = maxx, minn=base.val) # 我的右子树一定要比我自己大
        if condL and condR: return True  
        else: return False
        