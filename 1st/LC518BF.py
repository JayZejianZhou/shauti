class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        res = []
        if amount==0: return 1
        self.helper(amount, coins, res, [])
        
        return len(res)
        
        
    # res:结果序列的序列 resK: 暂时结果序列
    def helper(self, tar, nums, res, resK):
        resT = resK[:]
        if tar in nums:
                resT.append(tar)
                temp = self.saveAsDict(resT)
                if not temp in res: res.append(temp)
        for it in nums:            
            if tar-it>=nums[0]:
                resK.append(it)
                self.helper(tar-it, nums, res, resK)
                resK.pop()
                
            
            
            
    def saveAsDict(self, ls):
        res = collections.defaultdict(int)
        for it in ls:
            res[it] += 1
            
            
        return res