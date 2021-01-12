class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        if(strs.empty()){
            res.push_back({""});
            return res;
        }
        
        unordered_map<string, vector<string>> sorted;
        for(int i=0;i<strs.size();i++){
            string temp = strs[i];
            sort(strs[i].begin(), strs[i].end()); 
            sorted[strs[i]].push_back(temp);
        }
        
        for(auto it=sorted.begin(); it!=sorted.end(); it++){
            res.push_back(it->second);
        }
        
        return res;
    }
};