class Solution {
public:
    string decodeString(string s) {
        stack<char> helper;
        string res = "";
        for(int i=0;i<s.size();i++){
            if(s[i] != ']') helper.push(s[i]); 
            else{
                string temp_str = "";
                while(helper.top() != '['){ 
                    temp_str = helper.top()+temp_str;
                    helper.pop();
                }
                helper.pop(); //[出站
                int multiplier = 0; int decimal = 1;
                while(helper.size()>0 && helper.top()>='0' && helper.top()<='9') {
                    multiplier += (helper.top() -'0') * decimal;
                    helper.pop();
                    decimal*=10;
                }//pop the multiplier digit
                string temp_str2 = "";
                while(multiplier >0){ //重复括号里的字符
                    temp_str2 += temp_str;
                    multiplier--;
                }
                //计算出的字符重新进站
                for(int j=0;j<temp_str2.size();j++){
                    helper.push(temp_str2[j]);
                }
            }
        }
        
        //计算完成，全部提出站
        int the_size = helper.size();
        for(int i=0; i<the_size; i++){
            res = helper.top() + res;
            helper.pop();
        }
        return res;
    }
};