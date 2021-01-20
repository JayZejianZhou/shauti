class Solution {
private:
    int max_row;
    int max_col;
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area = 0; 
        max_row = grid.size(); max_col = grid[0].size();
        vector<vector<bool>> visited(max_row, vector<bool>(max_col, false));
        for(int i=0; i<max_row; i++){
            for(int j=0; j<max_col; j++){
                if(grid[i][j] == 1 && !visited[i][j]){                    
                    int this_size = helper(grid, visited, i, j, 0);
                    max_area = max(max_area, this_size);
                }
            }
        }
        
        return  max_area;
    }
    
    int helper(vector<vector<int>>& grid, vector<vector<bool>>& visited, int row, int col, int size){
        size++;
        visited[row][col] = true;
        if(col-1 >= 0 && !visited[row][col-1] && grid[row][col-1] == 1){
            size = helper(grid, visited, row, col-1, size);
        }
        if(col+1 < max_col && !visited[row][col+1] && grid[row][col+1] == 1){
            size = helper(grid, visited, row, col+1, size);
        }
        if(row-1 >= 0 && !visited[row-1][col] && grid[row-1][col] == 1){
            size = helper(grid, visited, row-1, col, size);
        }
        if(row+1 < max_row && !visited[row+1][col] && grid[row+1][col] == 1){
            size = helper(grid, visited, row+1, col, size);
        }
        return size;
    }
};