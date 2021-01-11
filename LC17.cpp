class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if(digits.empty()){
            return res;
        }
        helper(digits, res, "");
        return res;
    }
    
    void helper(string digits, vector<string>& res, string temp){
        if(digits.empty()){
            res.push_back(temp);
            return;
        }
        
        if(digits[0] == '1'){
            helper(digits.erase(0,1), res, temp);
        }else if(digits[0] == '2'){
            helper(digits.substr(1,digits.size()-1), res, temp+'a');
            helper(digits.substr(1,digits.size()-1), res, temp+'b');
            helper(digits.substr(1,digits.size()-1), res, temp+'c');
        }else if(digits[0] == '3'){
            helper(digits.substr(1,digits.size()-1), res, temp+'d');
            helper(digits.substr(1,digits.size()-1), res, temp+'e');
            helper(digits.substr(1,digits.size()-1), res, temp+'f');
        }else if(digits[0] == '4'){
            helper(digits.substr(1,digits.size()-1), res, temp+'g');
            helper(digits.substr(1,digits.size()-1), res, temp+'h');
            helper(digits.substr(1,digits.size()-1), res, temp+'i');
        }else if(digits[0] == '5'){
            helper(digits.substr(1,digits.size()-1), res, temp+'j');
            helper(digits.substr(1,digits.size()-1), res, temp+'k');
            helper(digits.substr(1,digits.size()-1), res, temp+'l');
        }else if(digits[0] == '6'){
            helper(digits.substr(1,digits.size()-1), res, temp+'m');
            helper(digits.substr(1,digits.size()-1), res, temp+'n');
            helper(digits.substr(1,digits.size()-1), res, temp+'o');
        }else if(digits[0] == '7'){
            helper(digits.substr(1,digits.size()-1), res, temp+'p');
            helper(digits.substr(1,digits.size()-1), res, temp+'q');
            helper(digits.substr(1,digits.size()-1), res, temp+'r');
            helper(digits.substr(1,digits.size()-1), res, temp+'s');
        }else if(digits[0] == '8'){
            helper(digits.substr(1,digits.size()-1), res, temp+'u');
            helper(digits.substr(1,digits.size()-1), res, temp+'v');
            helper(digits.substr(1,digits.size()-1), res, temp+'t');
        }else if(digits[0] == '9'){
            helper(digits.substr(1,digits.size()-1), res, temp+'w');
            helper(digits.substr(1,digits.size()-1), res, temp+'x');
            helper(digits.substr(1,digits.size()-1), res, temp+'y');
            helper(digits.substr(1,digits.size()-1), res, temp+'z');
        }        
    }
};