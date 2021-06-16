class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        x_num, o_num = 0, 0
        for it in board:
            temp = list(it)
            for jt in temp:
                if jt == "X": x_num+=1
                elif jt == "O": o_num+=1
        
        if o_num>x_num or x_num-o_num>1: return False
        
        win = self.check_win(board)
        
        if win=="X" and o_num==x_num: return False
        if win=="O" and x_num>o_num: return False
        
        return True
        
        
        
    # return o for O win, -1 for not win
    def check_win(self, board):
        # row win
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]: return board[i][2]
        
        # col win
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j]: return board[0][j]
        
        # diagnal win
        if board[0][0] == board[1][1] == board[2][2]: return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]: return board[0][2]
        
        return -1
        