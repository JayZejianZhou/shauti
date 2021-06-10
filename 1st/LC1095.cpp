/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        //二分法找出来中间值，看两边，arr[i]-arr[i-1]>0 和 arr[i]-arr[i+1]>0 同时成立
        int end=mountainArr.length()-1; int start=0; int mid=0;
        while(start+1<end){
            mid=start+(end-start)/2;
            int currentNum=mountainArr.get(mid);
            int lastNum=mountainArr.get(mid-1);
            int nextNum=mountainArr.get(mid+1);
            if(currentNum-lastNum>0 && currentNum-nextNum>0){
                break;
            }
            else if(currentNum-lastNum>0){
                start=mid;
            }
            else{
                end=mid;
            }
        }
        
        //二分法分两边查找
        int resLeft=binary_search(target, mountainArr, 0, mid, true);
        if(resLeft!=-1){
            return resLeft;
        }
        
        int resRight=binary_search(target, mountainArr, mid+1, mountainArr.length()-1, false);
        if(resRight!=-1){
            return resRight;
        }
        else{
            return -1;
        }
    }
    
    int binary_search(int target, MountainArray &mountainArr, int start, int end, bool isAssending){
        int mid=0;
        while(start+1<end){
            mid=start+(end-start)/2;
            int currentNum=mountainArr.get(mid);
            if(isAssending){//升序二分
                if(currentNum>target){
                    end=mid;
                }
                else if(currentNum<target){
                    start=mid;
                }
                else{
                    return mid;
                }
            }
            else{//降序二分
                if(currentNum>target){
                    start=mid;
                }
                else if(currentNum<target){
                    end=mid;
                }
                else{
                    return mid;
                }
            }
        }
        
        int startNum=mountainArr.get(start);
        int endNum=mountainArr.get(end);
        if(startNum==target){
            return start;
        }
        else if(endNum==target){
            return end;
        }
        else{
            return -1;
        }
    }
};