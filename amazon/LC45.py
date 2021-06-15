class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        
        min_steps = [float("inf")]*len(nums)
        min_steps[0] = 0
        for i in range(len(nums)):
            for j in range(i+1, i+1+nums[i]):
                if j>=len(nums): continue
                min_steps[j] = min(min_steps[i]+1, min_steps[j])
            
        return min_steps[-1]
                
            