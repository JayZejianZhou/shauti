class Solution {
    //请你把coner case分开写好
public:
    int findPeakElement(vector<int>& nums) {
        int start=0; int end=nums.size()-1; int mid=0;       
        
        while(start+1<end){
            mid=start+(end-start)/2;
            
            //corner case
            if(mid-1<0){
                return mid;
            }
            if(mid+1>=nums.size()){
                return mid;
            }
            
            
            if(nums[mid]-nums[mid-1]>0 && nums[mid]-nums[mid+1]>0){
                return mid;
            }
            else if(nums[mid]>=nums[mid-1]){
                start=mid;
            }
            else if(nums[mid]<nums[mid-1]){
                end=mid;
            }
          
        }
        
        //corner case
        if(start+1>=nums.size()){
            return mid;
        }
                    
        if(nums[start]>nums[start+1]){
            return start;
        }
        else{
            return end;
        }
    }
};