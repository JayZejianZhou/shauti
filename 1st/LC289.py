class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        res = [[None]*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                num_nb = self.getLiveNb(board, i, j)
                res[i][j] = board[i][j]
                if num_nb < 2:
                    res[i][j] = 0
                elif num_nb == 3:
                    res[i][j] = 1
                elif num_nb > 3:
                    res[i][j] = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = res[i][j]
        
    # get the number of live neighbours
    def getLiveNb(self, board, indr, indc):
        num = 0
        if self.nbs(board, indr-1, indc):
            num += 1    
        if self.nbs(board,indr-1, indc-1):
            num += 1 
        if self.nbs(board,indr-1, indc+1):            
            num += 1 
        if self.nbs(board,indr+1, indc):
            num += 1 
        if self.nbs(board,indr+1, indc-1):
            num += 1
        if self.nbs(board,indr+1, indc+1):
            num += 1 
        if self.nbs(board,indr, indc+1):
            num += 1 
        if self.nbs(board,indr, indc-1):
            num += 1 

        return num
                
    # get neighbour live, true or false
    def nbs(self, board, indr, indc):
        row = len(board)
        col = len(board[0])

        if indr < 0 or indc < 0 or indr >= row or indc >= col:
            return False
        else:
            if board[indr][indc] == 0:
                return False
            else:
                return True
            
            