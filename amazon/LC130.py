class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        visited = []
        for i in range(row):
            self.dfs(board, i, 0, row, col, visited)
            self.dfs(board, i, col-1, row, col, visited)
        for i in range(col):
            self.dfs(board, 0, i, row, col, visited)
            self.dfs(board, row-1, i, row, col, visited)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and not [i,j] in visited: 
                    board[i][j] = "X"
            
    def dfs(self, board, r, c, row, col, visited):
        if r<0 or r>=row or c<0 or c>=col:  return 0
        if board[r][c] == "X": return 0
        if [r,c] in visited: return 0
        visited.append([r,c])
        self.dfs(board, r-1, c, row, col, visited)
        self.dfs(board, r+1, c, row, col, visited)
        self.dfs(board, r, c-1, row, col, visited)
        self.dfs(board, r, c+1, row, col, visited)
                