class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int> res;
        int right= binary_search(arr, x);
        int left = right-1;
        do{
            if(is_left_closer(arr, left, right, x)){
                res.push_back(arr[left]);
                left --;
            }
            else{
                res.push_back(arr[right]);
                right++;
            }
        }while(res.size()<k);
        sort(res.begin(),res.end());
        return res;
    }
    
private:
    int binary_search(vector<int>& arr, int target){
        int start = 0;
        int mid=0;
        int end = arr.size()-1;
        while (start+1 < end){
            mid = start + (end - start)/2;
            if(arr[mid]>target){
                end = mid; 
            }
            else if(arr[mid]<target){
                start = mid;
            }
            else if (arr[mid]==target){
                start = end = mid;
            }
            else{
                return -1;
            }
        }
        return end;
    }
    
    bool is_left_closer(vector<int>& arr, int left, int right, int target){
        if(left<0){
            return false;
        }
        else if (right>=arr.size()){
            return true;
        }
        else{
            return abs(arr[left]-target)<= abs(arr[right]-target);
        }
    }
};