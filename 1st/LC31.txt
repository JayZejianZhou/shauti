# https://blog.csdn.net/fuxuemingzhu/article/details/82113409
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        numsb = nums[:] #back up the data
        # step 1: find the start to decrease item
        i = self.findDescending(nums)
        # discuss the conditions
        if i >= 0: 
            # find the number just larger than nums[i]
            j = len(nums)-1
            while nums[j] <= nums[i]: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        
        
        pass
        
        
        
    # 找到降序
    def findDescending(self, nums):
        i = len(nums)-2
        while i>=0 and nums[i+1] <=nums[i]: i-=1
            
        return i
        