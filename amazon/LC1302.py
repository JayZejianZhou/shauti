# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leaves = []
        
        self.dfs(root, leaves, 0, 0)
        
        leaves = sorted(leaves, key=lambda x:x[0], reverse = True)
        
        res_sum = 0
        for it in leaves:
            if it[0] == leaves[0][0]: res_sum += it[1].val
        
        return res_sum
        
    def dfs(self, base, leaves, depth, max_depth):
        if not base: return 0
        depth += 1
        if depth >= max_depth and not base.left and not base.right: leaves.append((depth, base))
        else:
            self.dfs(base.left, leaves, depth, max(max_depth, depth))
            self.dfs(base.right, leaves, depth, max(max_depth, depth))