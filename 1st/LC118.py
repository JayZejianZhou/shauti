class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        res.append([1])
        if numRows == 1:            
            return res
        res.append([1,1])
        if numRows == 2:            
            return res
        res.append([1,2,1])
        if numRows == 3:
            return res
        for i in range(3, numRows):
            res.append([1])
            for j in range(len(res[i-1])-1):
                res[i].append(res[i-1][j] + res[i-1][j+1])
            res[i].append(1)
            
        return res
        