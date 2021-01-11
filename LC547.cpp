class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int city_num = isConnected.size(); 
        vector<bool> visited(city_num, false);
        int res=0;
        for(int i=0; i<city_num; i++){
            if(!visited[i]){
                helper(isConnected, i, visited);
                res++;
            }
        }
        return res;
    }
    
    void helper(vector<vector<int>>& isConnected, int city_ind, vector<bool>& visited){       
        visited[city_ind] = true;
        for(int i=0; i<isConnected[city_ind].size(); i++){
            if(isConnected[city_ind][i] == 1 && !visited[i] && i!=city_ind){
                helper(isConnected, i, visited);
            }
        }
    }
};