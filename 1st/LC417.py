class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        self.row, self.col = len(heights), len(heights[0])
        resP, resA = [], []
        visitedP, visitedA = [], []
        for i in range(self.row): self.helper(heights, i, 0, resP, heights[i][0], None, None, visitedP)        
        for i in range(self.col): 
            self.helper(heights, 0, i, resP, heights[0][i], None, None, visitedP)
        for i in range(self.row): self.helper(heights, i, self.col-1, resA, heights[i][self.col-1], None, None, visitedA)
        for i in range(self.col): 
            self.helper(heights, self.row-1, i, resA, heights[self.row-1][i], None, None, visitedA)
            
        res = self.intersect(resP, resA)
        return res
    
    # stH: the height to compare, rLast, cLast, 从什么地方来的，visited最好记路径，因为需要的是路径
    def helper(self, heights, r, c, res, stH, rLast, cLast, visited):
        if c<0 or r<0 or c>=self.col or r>=self.row or [rLast, cLast, r, c] in visited or [r,c] in res: return None
        visited.append([rLast, cLast, r, c])
        if heights[r][c] >= stH: 
            res.append([r,c])
            self.helper(heights, r, c-1, res, heights[r][c], r, c, visited)
            self.helper(heights, r, c+1, res, heights[r][c], r, c, visited)
            self.helper(heights, r-1, c, res, heights[r][c], r, c, visited)
            self.helper(heights, r+1, c, res, heights[r][c], r, c, visited)
    
    def intersect(self, a, b):
        return [it for it in a if it in b]
    
        