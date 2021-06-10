class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)-3):
            remi = target - nums[i]
            for j in range(i+1, len(nums)-2):
                remj = remi - nums[j]
                for k in range(j+1, len(nums)-1):
                    remk = remj - nums[k]
                    for l in range(k+1, len(nums)):
                        reml = remk-nums[l]
                        if reml==0: 
                            resT = self.makeDict([nums[i], nums[j], nums[k], nums[l]])
                            if resT not in res:
                                res.append(resT)
        # decode dict
        resR = []
        for it in res:
            resT = []
            for key, val in it.items():
                resT += [key]*val
            resR.append(resT)
        return resR
    
    def makeDict(self, inD):
        res = collections.defaultdict(int)
        for it in inD: res[it]+=1
        return res