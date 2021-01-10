class Solution {
public:
    string minRemoveToMakeValid(string s) {
        vector<int> st;
        //if(s.back()<'a' || s.back()>'z' && s.back()!='(' && s.back()!=')') s.pop_back(); //编译器问题
        int left_num = 0;
        for(int i=0;i<s.size();i++){
            if(s[i] == '('){
                st.push_back(i);  
            }
            if(s[i] == ')'){
                if(st.empty()) s[i] = '*'; //没有左括号却出现了右括号，奇怪
                else {
                    st.pop_back();
                }
            }            
        }
        
        //再将没用完的'('都标*删除
        while(!st.empty()){
            s[st.back()] = '*';
            st.pop_back();
        }
        
        s.erase(remove(s.begin(), s.end(), '*'), s.end());
        return s;
    }
};