class Solution(object):    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.imageM = image  
        self.row_num = len(image)
        self.col_num = len(image[0])
        self.ori = image[sr][sc]
        
        if newColor == image[sr][sc]:
            return image
        
        self.helper(sr, sc, newColor)
        
        return self.imageM
        
        
    def helper(self, row, col, nc):
        self.imageM[row][col] = nc
        # up pixel
        if row-1 >= 0 and self.imageM[row-1][col] == self.ori:
            self.helper(row-1, col, nc)
        # down pixel
        if row+1 < self.row_num and self.imageM[row+1][col] == self.ori:
            self.helper(row+1, col, nc)
        # left pixel
        if col-1>= 0 and self.imageM[row][col-1] == self.ori:
            self.helper(row, col-1, nc)
        if col+1 < self.col_num and self.imageM[row][col+1] == self.ori:
            self.helper(row, col+1, nc)
            