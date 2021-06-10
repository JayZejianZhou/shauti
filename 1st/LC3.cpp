class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s=="") return 0;
        if(s.size()==1) return 1;
        
        vector<int> max_len(s.size(),0);//debug purpose
        int res=0;
        
        int j=1; int i=0;
        for(i=0;i<s.size()-1;i++){
            j=i;
            while(j<s.size()){
                string subs = s.substr(i,j-i+1);
                j++;
                if(subs.find(s[j]) != subs.npos){
                    max_len[i] = j-i;
                    res = max(res, j-i);
                    break;
                }
            }
            if(j==s.size()) res=max(res,j-i);
        }
        return res;
    }
};