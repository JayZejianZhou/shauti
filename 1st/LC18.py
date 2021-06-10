class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]: continue
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]: continue
                rem = target - nums[i] - nums[j]    # remaining value
                l, r = j+1, len(nums)-1
                while l<r:
                    if nums[l]+nums[r] == rem:
                        resT = [nums[i], nums[j], nums[l], nums[r]]
                        res.append(resT)
                        while l<r and l+1<len(nums) and nums[l]==nums[l+1]: l+=1
                        while l<r and r-1>0 and nums[r]==nums[r-1]: r-=1
                        l+=1
                    elif nums[l]+nums[r] > rem: r-=1
                    elif nums[l]+nums[r] < rem: l+=1
            
        return res
    