#include <iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i; int j; bool isDone = false; vector<int> res(2, 0);
        for (i = 0; i < int(nums.size()); i++) {
            for (j = 0; j < int(nums.size()); j++) { // see if it satisfy the condition
                if ((nums[i] + nums[j] == target) && i != j) {
                    res[0] = nums[i]; res[1] = nums[j];
                    break;
                }
                isDone = true;
            }
            if (isDone) {
                break;
            }
        }
        return nums;
    }
};

int main() {
    int* a = new int[2, 7, 11, 15]; vector<int> tt;
    vector<int> input(a, a+4); 
    Solution sol;
    tt=sol.twoSum(input,9);

    return 0;
}


