class Solution {
//dfs, recursive solution, binary tree, true or false
public: 
    vector<vector<int>> subsets(vector<int>& nums) {
        //sort the vector 
        sort(nums.begin(), nums.end());
        
        vector<vector<int>> res;
        vector<int> subset;
        //perform dfs
        dfs(nums, 0, subset, res);
        
        return res;
        
    }
private:
    void dfs(vector<int> nums, int currentIndex, vector<int> &subset, vector<vector<int>> &res){
        res.push_back(subset); //store the subset
        for(int i=currentIndex; i<nums.size(); i++){
            subset.push_back(nums[i]); //add current to the subset
            dfs(nums, i+1, subset, res); //站在现在的节点，开始进行下一轮dfs
            subset.pop_back(); //why remove the last one?
            //pop_back 是因为要返回父节点，本节点要删除
            //排除重复是因为i=currentIndex；相当于现在统计过的就不再统计了，如果是排列的话，那就是i=0; 
        }
    }
};