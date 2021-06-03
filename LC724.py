class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)):
            if i == 0:
                left = 0
                right = sum(nums[1:])
            elif i == len(nums)-1:
                left = sum(nums[0:-1])
                right = 0
            else:
                left = sum(nums[:i])
                right = sum(nums[i+1:])
            if left == right:
                return i
            
        return -1