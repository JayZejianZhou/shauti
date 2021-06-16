class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_cp = nums[:]
        nums.sort()
        
        l, r = 0, len(nums)-1
        while nums[l] == nums_cp[l] and l<r: l+=1
        while nums[r] == nums_cp[r] and l<r: r-=1
        
        return r-l+1 if l!=r else 0