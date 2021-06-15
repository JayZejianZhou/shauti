class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)): nums[i] = str(nums[i])   
        nums.sort(cmp=self.cmpr, reverse=True)
        if nums[0]=="0": return "0"
        
        res = ""
        for i in range(len(nums)): res += nums[i] 
        return res
            
    def cmpr(self, x, y):
        if x==y: return 0
        for i in range(min(len(x), len(y))):
            if x[i] > y[i]: return 1
            elif x[i] < y[i]: return -1
        
        if len(x) < len(y):      return self.cmpr(x, y[i+1:])
        elif len(y) < len(x):    return self.cmpr(x[i+1:], y)       
        else: return 0
            