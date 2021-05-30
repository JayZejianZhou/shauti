class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cur_len = len(nums)
        for i in range(len(nums)):
            if i < cur_len and nums[i] == 0 :                
                while i < cur_len and nums[i] == 0:
                    cur_len -= 1
                    nums = self.move_ahead(nums, i)
        
    def move_ahead(self, nums, ind):
        for i in range(ind, len(nums)-1):
            nums[i] = nums[i+1]
        nums[-1] = 0
        return nums