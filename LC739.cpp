//https://leetcode-cn.com/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size());
        stack<int> stk;
        
        for(int i=0;i<T.size();i++){
            if(stk.empty()) stk.push(i);
            else{
                while(!stk.empty() && T[stk.top()] < T[i]){
                    auto t= stk.top();
                    res[t] = i-t;
                    stk.pop();
                    
                }
                stk.push(i);
            }
            
        }
        
        return res;
    }
};