// 有点小问题，run和debug结果不一样
class Solution {
private: 
    int is_duplicate(string s, int k){
        if(s.size() < k) return -1;
        for(int i=0; i<s.size()-k; i++){
            int j=1;
            while(s[i] == s[i+j]) {
                if(j==k-1) return i;
                j++;
            }
        }
        return -1;
    }
    
public:
    string removeDuplicates(string s, int k) {
        while(true){
            int res=is_duplicate(s,k);
            if(res == -1) return s;
            else{
                s.erase(s.begin()+res,s.begin()+res+k);
            }
        }       
        
    }
};