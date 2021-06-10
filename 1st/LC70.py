class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # DP function: dp[i] = dp[i-1] + dp[i-2]
        # dp[i] possible ways to climb
        
        if n<=1:
            return 1
        
        dp = [None] * n
        dp[0] = 1
        dp[1] = 2
        
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]