class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_t = 0
        res = []
        for i in nums:
            sum_t += i
            res.append(sum_t)
        return res