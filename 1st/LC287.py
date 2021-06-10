class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = dict()
        for it in nums:
            if it in data: return it
            else: data[it] = 0
        