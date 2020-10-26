class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i; int j; bool isDone = false; vector<int> res(2, 0);
        for (i = 0; i < int(nums.size()); i++) {
            for (j = 0; j < int(nums.size()); j++) { // see if it satisfy the condition
                if ((nums[i] + nums[j] == target) && i != j) {
                    res[0] = i; res[1] = j;
                    break;
                    isDone = true;
                }
                
            }
            if (isDone) {
                break;
            }
        }
        return res;
    }
};
