class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        unordered_map<int, int> time_num;
        int sum_num = 0;
        for(int i=0; i<time.size(); i++){
            for(int j=0; j<=16; j++){
                int lat=j*60;
                auto it = time_num.find(lat- time[i]);
                if(time[i] < lat && it!=time_num.end()) {
                    sum_num+=it->second; 
                }
            }
            time_num[time[i]]++;
        }
        
        return sum_num;
    }
};