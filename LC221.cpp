class Solution {
private:
    int m;
    int n;
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        m=matrix.size(); n=matrix[0].size();
        if(m==1 && n==1) return (matrix[0][0] == '0') ? 0:1;
        vector<vector<bool>> visited(m, vector<bool>(n,false));
        int max_expansion = 0;
        //找到1以后扩张一个反L型 
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(matrix[i][j]=='1'){
                    int expansion=1;
                    while(helper(matrix, i, j, expansion)) expansion++;
                    max_expansion = max(max_expansion, expansion);
                }
            }
        }
        
        return pow(max_expansion, 2);
    }
    
    bool helper(vector<vector<char>>& matrix, int row, int col, int expansion){
        if(row+expansion>=m || col+expansion>=n) return false;
        for(int i=row; i<=row+expansion; i++){
            if(matrix[i][col+expansion] == '0') return false;
        }
        for(int j=col; j<=col+expansion; j++){
            if(matrix[row+expansion][j] == '0') return false;
        }
        return true;
    }
};