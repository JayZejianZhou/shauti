class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 0
        while True:
            if all([nums[0]==it for it in nums]): return steps          
            nums.sort()  
            # 找到开始不一样的点
            i = len(nums)-1
            while nums[i] == nums[-1]: i -= 1
            addN = (nums[-1]-nums[i])
            for j in range(len(nums)-1): nums[j]+=addN  # 每个加1
            steps += addN
            
        