class Solution {
public:
    string longestPalindrome(string s) {
        int max_len=0; string res=""; int start=0;
        if(s=="") return "";
        if(s.length()==1) return s;
        for(int i=0;i<s.length()-1;i++){
            search_palin(s, i, i, start, max_len, res );
            search_palin(s, i, i+1, start, max_len, res);
        }
        return res;
    }
    
    void search_palin(string s, int left, int right, int& start, int& max_len, string& res){
        while(left>=0 && right<s.length() && s[left]==s[right]){
            left--;right++;
        }
        start = left+1;
        int len=right-left-1;
        if(len>max_len){
            max_len=len;
            res = s.substr(start, max_len);
        }
    }
};