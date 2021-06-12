class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i<len(nums):
            if nums[i] == val:
                if i == len(nums)-1: nums.pop()
                else:
                    for j in range(i, len(nums)-1): nums[j]=nums[j+1]
                    nums.pop()
            else:
                i += 1
        