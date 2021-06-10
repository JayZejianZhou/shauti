# https://blog.csdn.net/qq_37821701/article/details/107333410

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """        
        if len(s) == 1:
            return 0
        
        res = 0
        resL = []
        for i in range(len(s)-1):
            if not s[i] == s[i+1]:
                resN, resLT = self.findP(s, i)
                res += resN
                resLT = resL + resLT
        
        return res
                
                
    # 向左向右查找0和1
    def findP(self, s, ind):
        res = 0
        resL = []
        l, r = ind, ind+1
        lc, rc = s[ind], s[ind+1]
        while s[l] == lc and s[r] == rc:
            res += 1
            resL.append([l,r])
            if l-1 < 0 or r+1 >= len(s):
                return res, resL
            else:
                l -= 1
                r += 1
        return res, resL