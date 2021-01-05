class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        
        if(words.size() == 1) return true;
        
        int j=0; int left_words=words.size();
        for(int i=0;i<words.size()-1;i++){
            if(!isPreLefter(words[i], words[i+1], order)) return false;
        }
        return true;
    }

    bool isPreLefter(string s1, string s2, string order){
        int i=0;
        while(i<max(s1.size(), s2.size())){
            if(i==s1.size() && i<s2.size()) return true;
            else if(i==s2.size() && i<s1.size()) return false;
            if(order.find(s1[i]) > order.find(s2[i])) return false;
            else if(order.find(s1[i]) < order.find(s2[i])) return true;
            i++;
        }
        return true;
    }
};