# https://blog.csdn.net/fuxuemingzhu/article/details/83504437
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # greedy
        reach_max = [0]*len(nums)
        reachable = [False]*len(nums)
        reachable[0] = True 
        if len(nums) == 1: return True
        for i in range(len(nums)-1):
            if not reachable[i]: return False
            reachable[i+1:i+nums[i]+1] = [True]*nums[i]
            if reachable[-1] == True: return True
        