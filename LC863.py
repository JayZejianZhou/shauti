# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        # 子树
        res = []
        self.dfs(target, k, res)

        
        # 母树
        # find the base of target
        if not target == root:
            ma = []
            self.helper(root, target, ma)
            ma = ma[::-1]
            for i in range(len(ma)):
                if ma[i].left==target or ma[i].left in ma:
                    self.dfs(ma[i], k-i-1, res, avoid="left") 
                elif ma[i].right==target or ma[i].right in ma:
                    self.dfs(ma[i], k-i-1, res, avoid="right")
                else:
                    self.dfs(ma[i], k-i-1, res)
        
        # 邻居
        if k >= 2 and not target == root:
            ma = []
            self.helper(root, target, ma)
            ma = ma[::-1]
            if ma[0].right==target:
                self.dfs(ma[0].left, k-2, res) 
            else:
                self.dfs(ma[0].right, k-2, res) 
            
            
        # 把自己本身除掉
        while target.val in res and not k==0:
            res.remove(target.val)
            
        return res
        
        
    def dfs(self, base, k, res, avoid=None): # 最后一个是avoid找左还是右子树，防止往母树上找的时候再找回来
        if not base: return 0
        if k == 0 : 
            if base.val in res: return 0
            else: return res.append(base.val)
        if not avoid == "left": self.dfs(base.left, k-1, res) 
        if not avoid == "right": self.dfs(base.right, k-1, res) 
        
    # traverse to find 母树链
    def helper(self, base, tar, ma):
        if not base: return False
        if base.left==tar or base.right==tar: 
            ma.append(base)
            return True
        else: 
            ma.append(base)
            res1 = not self.helper(base.left, tar, ma)
            res2 = not self.helper(base.right, tar, ma)
            if res1 and res2:
                ma.pop()
            else:
                return True