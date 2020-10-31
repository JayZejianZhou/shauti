/*（2）如果nums[low]<=nums[mid]，那么说明从low到mid一定是有序的，那么我们只需要判断target是不是在low到mid之间，如果是则把右边缘移到mid-1，否则target就在另一半，即把左边缘移到mid+1。
（3）如果nums[low]>nums[mid]，那么说明从mid到high一定是有序的，那么我们只需要判断target是不是在mid到high之间，如果是则把左边缘移到mid+1，否则就target在另一半，即把右边缘移到mid-1。*/

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // binary search for the changing point
        int start = 0;
        int end = nums.size()-1;
        int mid= 0;
        while(start+1<end){
            mid = start+(end-start)/2;
            if(is_first(nums, mid)){
               break; 
            }
            else if(nums[start]<nums[mid]){
                start=mid;
            }
            else if(nums[start]>nums[mid]){
                end=mid;
            }
        }
        
        int resLeft=binary_search(nums,0,mid-1,target);
        int resRight=binary_search(nums,mid,nums.size()-1,target);
        
        if(resLeft!=-1 ){
            return resLeft;
        }
        else if (resRight!=-1){
            return resRight;
        }
        else{
            return -1;
        }
    }
    
private:
    bool is_first(vector<int>& nums, int pos){
        if(pos==0){
            return true;
        }
        else if(nums[pos] >= nums[pos-1] ){
            return false;
        }
        else{
            return true;
        }
    }
    int binary_search(vector<int>& nums, int start, int end, int target) {
        //corner case
        if(start<0 || end<0){
            if(nums[0]==target){
                return 0;
            }
            else{
                return -1;
            }
        }
        
        // binary search
        int mid= 0;
        while(start+1<end){
            mid = start+(end-start)/2;
            if(nums[mid]>target){
                end=mid;
            }
            else if(nums[mid]<target){
                start=mid;
            }
            else{
                start=end=mid;
            }
        }
        if(nums[start]==target){
            return start;
        }
        else if(nums[end]==target){
            return end;
        }
        else{
            return -1;
        }
    }
};