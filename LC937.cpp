class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> digits;
        vector<string> strs;
        if(logs.empty())  return strs;
        if(logs.size() == 1){
            strs.push_back(logs[0]);
            return strs;
        }

        for(int i=0; i<logs.size(); i++){
            int j=0;
            while(logs[i][j]!=' ') j++;
            if(logs[i][j+1]>='0' && logs[i][j+1]<='9') digits.push_back(logs[i]);
            else  strs.push_back(logs[i]);
        }
        //排序
        
        if(strs.size() >= 1){
            for(int i=0; i<strs.size()-1; i++){
                for(int j=0; j<strs.size()-1-i; j++){
                    if(is_bigger(strs[j], strs[j+1])){
                        string temp = strs[j];
                        strs[j] = strs[j+1];
                        strs[j+1] = temp;
                    }
                }
            }
        }
        
        //把数字log插回去
        strs.insert(strs.end(), digits.begin(), digits.end());
        return strs;
    }
    
    bool is_bigger(string s1, string s2){
        int i=0, j=0;
        while(s1[i]!=' ') i++;
        while(s2[j]!=' ') j++;
        string indexer1 = s1.substr(0, i);
        string indexer2 = s2.substr(0, j);
        while(i<s1.size() && j<s2.size()){
            if(s1[i]<s2[j]) return false;
            else if(s1[i]>s2[j]) return true;
            else{
                i++; j++;
            }
        }
        if(i==s1.size() && j!=s2.size()) return false;
        if(i!=s1.size() && j==s2.size()) return true;
        
        i=0;j=0;
        while(i<indexer1.size() && j<indexer2.size()){
            if(indexer1[i]<indexer2[j]) return false;
            else if(indexer1[i]>indexer2[j]) return true;
            else{
                i++; j++;
            }
        }
        if(i==indexer1.size() && j!=indexer2.size()) return false;
        if(i!=indexer1.size() && j==indexer2.size()) return true;
        
        return false;
    }
};