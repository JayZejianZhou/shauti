class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(int)
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        # count the nums frequency
        num_count = collections.defaultdict(int)
        for i in range(len(nums)):
            num_count[nums[i]] += 1
        
        # initial dp
        dp[0] = num_count[0]*0
        # find second not-same number
        dp[1] = num_count[1]*1
        # perform dynamic programing
        for i in range(2, nums[-1]+1):
            dp[i] = max(dp[i-1], dp[i-2]+num_count[i]*i)
        
        return dp[dp.keys()[-1]]