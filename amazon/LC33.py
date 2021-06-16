class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==1 and nums[0]==target: return 0
        if len(nums)==1 and nums[0]!=target: return -1
        
        # find the pivit index
        i = 1
        while i<len(nums) and nums[i] > nums[i-1]: i += 1
        
        searchl = self.binary_search(nums[:i], target)
        searchr = self.binary_search(nums[i:], target)
        
        if searchl != -1: return searchl
        elif searchr != -1: return searchr+i
        else: return -1
        
        
        
    def binary_search(self, nums, tar):
        if not len(nums): return -1
        if tar < nums[0] or tar>nums[-1]: return -1
        l, r = 0, len(nums)-1
        while l+1<r:
            mid = (l+r)//2
            if nums[mid]<tar: l = mid
            elif nums[mid]>tar: r = mid
            else: return mid
        
        if nums[l]==tar: return l
        if nums[r]==tar: return r
        return -1
                
            