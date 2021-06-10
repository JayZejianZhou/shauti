class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        vector<vector<int>> res;
        priority_queue< pair<double, vector<int>>, vector<pair<double, vector<int>>>, greater<pair<double, vector<int>>> > distances;
        for(auto itc:points) distances.push({sqrt(pow(itc[0],2)+pow(itc[1],2)), itc});
        for(int i=0;i<K;i++){
            res.push_back(distances.top().second);
            distances.pop();
        }
        return res;
    }
};