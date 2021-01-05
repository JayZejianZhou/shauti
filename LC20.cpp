//用栈
class Solution {
public:
    bool isValid(string s) {
        
        if(s.size()==1) return false;
        
        list<char> temp;
        for(int i=0;i<s.size();i++){
            if(s[i]=='(' || s[i]=='{' || s[i]=='['){
                temp.push_front(s[i]);
            }else{
                if(s[i]==')' && temp.front()!='(') return false;
                else if (s[i]==']' && temp.front()!='[') return false;
                else if (s[i]=='}' && temp.front()!='{') return false;
                else temp.pop_front();
            }
        }
        if(temp.size()==0)     return true;
        else                    return false;
    }
};