# https://blog.csdn.net/fuxuemingzhu/article/details/82845212
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0]*(amount+1)
        dp[0] =1
        for coin in coins:
            for i in range(1, amount+1):
                if i >= coin: dp[i] += dp[i-coin]
        return dp[amount]
        