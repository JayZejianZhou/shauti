class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int row = matrix.size()-1; int col = matrix[0].size()-1;
        vector<int> res;
        if(row==0 && col==0){
            res.push_back(matrix[0][0]);
            return res;
        }
        int matrix_size = (row+1)*(col+1);
        
        int row_f=0; int col_f=0;
    
        while(true){ 
            if(res.size()>=matrix_size){
                break;
            }
            
            // 上
            if(col-col_f>0 ){
                for(int i=col_f; i<=col; i++) res.push_back(matrix[row_f][i]);
                row_f++;
            }
            if(res.size()>=matrix_size){
                break;
            }
            // 右
            if(row-row_f>0 ){
                for(int i=row_f; i<=row; i++) res.push_back(matrix[i][col]);
                col--;
            }
            if(res.size()>=matrix_size){
                break;
            }
            //下
            if(col-col_f>0 ){
                for(int i=col; i>=col_f; i--) res.push_back(matrix[row][i]);
                row--;
            }
            if(res.size()>=matrix_size){
                break;
            }
            //左
            if(row-row_f>0){
                for(int i=row; i>=row_f; i--) res.push_back(matrix[i][col_f]);
                col_f++;
            }
            if(res.size()>=matrix_size){
                break;
            }
        }
        return res;
    }
};