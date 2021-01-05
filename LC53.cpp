class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res = INT_MIN, curSum = 0;
        for (int num : nums) {
            curSum = max(curSum + num, num);//算到i位置，是之前的和大还是数本身大。如果数本身比求和大，那就没必要再保留前面的求和了。
            res = max(res, curSum);
        }
        return res;
    }
};