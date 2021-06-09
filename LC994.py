class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """       
        
        # list of not rot and rot oragens
        nr, rt = [], []
        flag_no_neig = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: nr.append([i,j])
                if grid[i][j] == 2: rt.append([i,j])
        if not nr: return 0     # 没有好的
        if not rt: return -1    # 没有烂的

        
        # start 
        last = rt[:]
        time = 0
        while nr:
            new = []
            while last:
                new = new + self.rot(grid, last[0][0], last[0][1], nr)
                last.pop(0)
            last = new[:]
            time += 1
            
            if not new and nr: return -1    # 剩下来的好橘子碰不到了
        
        return time
            
            
#     # check if has neighbours
#     def is_nei(self, grid, r, c):
#         row, col = len(grid), len(grid[0])
#         condi = []
#         if r-1>=0 and c>=0: condi.append(grid[r-1][c]>0)
#         if r+1<row and c>=0: condi.append(grid[r+1][c]>0)
#         if r<row and c+1<col: condi.append(grid[r][c+1]>0)
#         if r<row and c-1>=0: condi.append(grid[r][c-1]>0)        
        
#         return any(condi)
           
    # rot the neighbours, Ture has, Flase, not
    def rot(self, grid, r, c, nr):
        row, col = len(grid), len(grid[0])
        new = []
        if r-1>=0 and c>=0 and grid[r-1][c]==1: 
            grid[r-1][c]=2
            nr.remove([r-1, c])
            new.append([r-1,c])
        if r+1<row and c>=0 and grid[r+1][c]==1: 
            nr.remove([r+1, c])
            grid[r+1][c]=2
            new.append([r+1,c])
        if r>=0 and c-1>=0 and grid[r][c-1]==1: 
            grid[r][c-1]=2
            nr.remove([r, c-1])
            new.append([r,c-1])
        if r>=0 and c+1<col and grid[r][c+1]==1: 
            grid[r][c+1]=2
            nr.remove([r, c+1])
            new.append([r,c+1])
        return new