class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int mid = 0;
        int start = 0;
        int end = arr.size();
        vector<int> res;
        
        //sort the mother fucker
        sort(arr.begin(), arr.end());
        
        //binary search
        while(start+1 < end){
            mid = start + (end - start)/2;
            if(arr[mid] < x){
                start = mid;
            }
            else if(arr[mid] > x){
                end = mid;
            }
            else{
                start = end = mid;
            }
        }
        

        
        //insert the numbers
        int insertPosStart, insertPosEnd;
        if (start == end){
            insertPosStart = end-round(k/2);
            insertPosEnd = end+k/2;
            res.insert(res.begin(), arr.begin()+insertPosStart, arr.begin()+insertPosEnd);
        }
        else if(arr[start] == x){
            insertPosStart = start-round((k-1)/2);
            insertPosEnd = start+(k-1)/2;
            res.insert(res.begin(), arr.begin()+insertPosStart, arr.begin()+insertPosEnd);
        }
        else if (arr[end] == x){
            insertPosStart = end-round((k-1)/2);
            insertPosEnd = end+(k-1)/2;
            res.insert(res.begin(), arr.begin()+insertPosStart, arr.begin()+insertPosEnd);
        }
        else{
            if(k==1){
                res.push_back(arr[start]);
            }else{
                insertPosStart = start-round(k/2);
                insertPosEnd = start+k/2;
                res.insert(res.begin(), arr.begin()+insertPosStart, arr.begin()+insertPosEnd);
            }
        }
        return res;
    }

};