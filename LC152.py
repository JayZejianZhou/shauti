# https://blog.csdn.net/camellhf/article/details/71104508
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # dp[i][0] max, dp[i][1] min
        dp = [[None, None]]*len(nums)
        dp[0][0], dp[0][1] = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i])
            dp[i][1] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i])
            res = max(res, dp[i][0])
        return res