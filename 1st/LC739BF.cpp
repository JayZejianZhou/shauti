class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size(),0);
        for(int i=0; i<T.size()-1; i++){
            int j=i+1;
            while(T[i] >= T[j]){
              j++;
                if(j==T.size()){
                    j=i;
                    break;
                }
            } 
            res[i] = j-i;
        }
        return res;
    }
};