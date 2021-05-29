class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = float('inf')
        res_sum = 0
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                sumT = nums[i] + nums[left] + nums[right]
                if abs(sumT - target) < res:
                    res = abs(sumT - target)
                    res_sum = sumT
                if sumT > target:
                    right -= 1
                elif sumT < target:
                    left += 1
                else:
                    return res_sum
        return res_sum
                