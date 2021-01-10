class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<char> help;
        string res = "";
        //if(s.back()<'a' || s.back()>'z' && s.back()!='(' && s.back()!=')') s.pop_back(); //编译器问题
        int left_num = 0;
        for(int i=0;i<s.size();i++){
            if(s[i] == '('){
                left_num++;   
            }
            if(s[i] == ')'){
                if(left_num == 0) continue; //没有左括号却出现了右括号，奇怪
                else {
                    left_num--;
                }
            }            
            help.push(s[i]);
        }
        
        //再倒着来一下
        stack<char> helper2;
        int right_num = 0;        
        while (!help.empty()){
            if(help.top() == ')'){
                right_num++;   
            }
            if(help.top() == '('){
                if(right_num == 0) {help.pop();continue;} //没有左括号却出现了右括号，奇怪
                else {
                    right_num--;
                }
            }            
            helper2.push(help.top());
            help.pop();
        }
        
        //从栈提出来
        while (!helper2.empty()){
            res=res+helper2.top();
            helper2.pop();
        }
        
        return res;
    }
};