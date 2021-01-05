//recursive会有重复的麻烦
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        if(nums.size()<=1) return res;
        
        sort(nums.begin(), nums.end());
        for(int i=0;i<nums.size()-2;i++){
            int j=i+1;
            while(j<nums.size()-1){
                int k=j+1;
                while(k<nums.size()){
                    if(nums[i]+nums[j]+nums[k]==0) res.push_back({res[i], res[j], res[k]});
                    else if(nums[i]+nums[j]+nums[k]>0) break;
                    else if(nums[i]+nums[j]+nums[k]<0) k++;
                }
            }
        }
    return res;
        
    }
};