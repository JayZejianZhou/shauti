class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        for i,it in enumerate(nums):
            if i != it:
                return i
        return len(nums)
            