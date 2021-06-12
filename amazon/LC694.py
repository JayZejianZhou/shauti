class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        visited = []
        island = []
        row, col = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not [i,j] in visited and not grid[i][j] == 0:
                    res += 1
                    temp = []
                    self.dfs(grid, i, j, row, col, temp)
                    visited += temp
                    island.append(temp[:])
        
        # check same ilands
        rm = []
        i = 0
        while i < len(island)-1:
            j=i+1
            while j < len(island):
                if self.check_same(island[i], island[j]): island.pop(j)
                else: j+=1
            i+=1
        
        res = len(island)
                    
        
        return res
    
    
    def check_same(self, a, b):
        if not len(a)==len(b): return False
        for i in range(1, len(a)):
            if not a[i][0] - b[i][0] == a[i-1][0] - b[i-1][0] or not a[i][1] - b[i][1] == a[i-1][1] - b[i-1][1]: return False
        return True
        
    def dfs(self, grid, r, c, row, col, visited):
        if r<0 or c<0 or r>=row or c>=col: return 0
        if grid[r][c] == 0: return 0
        if [r,c] in visited: return 0
        visited.append([r,c])
        self.dfs(grid, r-1,c, row, col, visited)
        self.dfs(grid, r+1,c, row, col, visited)
        self.dfs(grid, r, c-1, row, col, visited)
        self.dfs(grid, r, c+1, row, col, visited)
        
        