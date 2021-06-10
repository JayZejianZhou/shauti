class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 所有元素里只能有一个降序，并且把那一个剔除掉之后，就可以变成升序
        dNum = 0
        for i in range(0, len(nums)-1):
            if nums[i+1] < nums[i]:
                if i==0: nums[i] = nums[i+1]
                elif nums[i+1]>=nums[i-1]: nums[i] = nums[i-1]
                else : nums[i+1] = nums[i]
                dNum += 1
                
        
        if dNum > 1: return False
        else: return True
            
        