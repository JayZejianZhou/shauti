class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        visited = []
        regions = []
        for i in range(1, row-1):
            for j in range(1, col-1):
                temp = [False, []]  # is at boarder?
                self.dfs(board, i, j, row, col, visited, temp)
                if not temp[0]: regions.append(temp[1])
        
        # capture
        for it in regions:
            for jt in it: board[jt[0]][jt[1]] = "X"
                
                
    def dfs(self, board, r, c, row, col, visited, temp):
        if r<0 or c<0 or r>=row or c>=col: return 0
        if board[r][c] == "X": return 0
        if [r,c] in visited: return 0
        if r ==0 or r==row-1 or c==0 or c==col-1: temp[0]=True  # this is the boarder 
        temp[1].append([r,c])
        visited.append([r,c])
        self.dfs(board, r+1, c, row, col, visited, temp)
        self.dfs(board, r-1, c, row, col, visited, temp)
        self.dfs(board, r, c+1, row, col, visited, temp)
        self.dfs(board, r, c-1, row, col, visited, temp)
        
        