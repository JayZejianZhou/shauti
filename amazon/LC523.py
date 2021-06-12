# https://www.youtube.com/watch?v=C2xC-EnvpaQ&ab_channel=happygirlzt
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        rSum = [0]*len(nums)    # running sum
        data = dict() # remain-sum_ind pair
        
        rSum[0] = nums[0]
        data[rSum[0] % k] = 0
        for i in range(1, len(nums)):        
            rSum[i] = rSum[i-1] + nums[i]
            
            # corner case, 0 is always true
            if i>1 and rSum[i] == rSum[i-2]:return True
            
            rem = rSum[i] % k
            if rem == 0: return True
            elif rem in data and i - data[rem] >= 2: return True
            else: data[rem] = i
                
        
        return False
        