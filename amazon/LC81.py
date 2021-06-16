class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums)==1: return nums[0]==target
        # find pivot index
        i = 1
        while i<len(nums) and nums[i] >= nums[i-1]: i+=1
            
        # binary search
        return self.bs(nums[:i], target) or self.bs(nums[i:], target)
        
        
    def bs(self, nums, target):
        if not nums: return False
        if target<nums[0] or target>nums[-1]: return False
        l, r = 0, len(nums)-1
        while l+1<r:
            mid = (l+r)//2
            if nums[mid]<target: l=mid
            elif nums[mid]>target: r=mid
            else: return True
        
        if nums[l] == target: return True
        elif nums[r] == target: return True
        else: return False