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
        
        //循环insert
        int indMin=0;
        bool flagStart=false; //start hit the begininng
        bool flagEnd=false; //end hit the end

        
        do{
            indMin = argmin(abs(arr[start]-x), abs(arr[end]-x), start, end);
            if(indMin==start && !flagStart){
                res.push_back(arr[start]);
                if(start>0){
                    start--;
                }
                else{
                   flagStart = true; 
                }
                
            }
            else if(indMin == end && !flagEnd){
                res.push_back(arr[end]);
                if (end >= arr.size() -1){
                    flagEnd = true;                    
                }
                else{
                    end++;
                }
                
            }
            else{
                res[0]=-1;
                return res;
            }

        }while (res.size()<k);
        
        sort(res.begin(), res.end());
        return res;
    }
    
    private:
       int argmin(int a, int b, int indA, int indB){
           if(a>b){
               return indB;
           }
           else{
               return indA;
           }
     } 
};