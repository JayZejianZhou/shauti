class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find degree
        deg_count = collections.defaultdict(int)
        for i in nums:
            deg_count[i] += 1

        degM = max(deg_count.values())  # the value of the maximum degree
        # get the numbers of the maximum degree
        numM = []
        min_sub = float('inf')
        for key, val in deg_count.items():
            if val == degM:
                # find the first occurance
                indl = nums.index(key)
                # find the last occurance
                nums_fl = nums[::-1]    # flip the nums
                indr = len(nums) -1 - nums_fl.index(key)
                # calculate the difference
                dif = indr - indl
                if dif < min_sub:
                    res = nums[indl:indr+1]
                    min_sub = dif
        
        return len(res)
        pass
        