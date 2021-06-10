class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.sort()
        verticalCuts.sort()
        diffH = self.cont_minus([0]+horizontalCuts+[h])
        diffV = self.cont_minus([0]+verticalCuts+[w])
        
        return max(diffH) * max(diffV) % (10 ** 9 + 7)
        
        
    # 递减函数
    def cont_minus(self, a):
        res = []
        for i in range(len(a)-1):
            res.append(a[i+1] - a[i])
        return res