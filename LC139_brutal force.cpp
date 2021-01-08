class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        bool is_in=false;
        //建立一个字典首字母表来减少计算力
        unordered_map<char, vector<string>> dict_data;
        for(int i=0;i<wordDict.size();i++){
            dict_data[wordDict[i][0]].push_back(wordDict[i]);
        }
        
        return helper(s, dict_data);
    }
    
    bool helper(string s, unordered_map<char, vector<string>> & dict_data){
        if(s.back()<'a' || s.back()>'z') s.pop_back(); //字符串都要注意最后一个'/'
        // if(s.size() == 0) return true;
        if(dict_data.find(s[0]) == dict_data.end()) return false;
        
        bool temp_in = false;
        for(int i=0; i<dict_data[s[0]].size(); i++){
            if(s.size() < dict_data[s[0]][i].size()) continue; //s剩下来的字符不够字典了
                string sub_temp = s.substr(0, dict_data[s[0]][i].size()); //取与字典存的字符串相等的字符串，再比较是不是相等
                if(sub_temp == dict_data[s[0]][i]){
                    bool temp2 = false;
                    if(dict_data[s[0]][i].size() == s.size()) temp2 = true;
                    else temp2 = helper(s.substr(dict_data[s[0]][i].size(), s.size()), dict_data);
                    temp_in |= temp2;
                }
        }
        return temp_in;
    }
    
};