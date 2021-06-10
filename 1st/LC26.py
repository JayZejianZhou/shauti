class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 1:
            return len(nums)
        
        for i in range(len(nums)-1):
            if i >= len(nums)-1:
                break
            self.helper(i, nums)
        return len(nums)
                
        
    def helper(self, ind, nums):
        if ind+1<len(nums) and nums[ind] == nums[ind+1]:
            nums.pop(ind)
            self.helper(ind, nums)
            
        