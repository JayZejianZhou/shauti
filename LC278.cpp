// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    long firstBadVersion(long n) {
        long i=0;
        long start=0; 
        long end=n; 
        long mid=0;
        while (i+1<n){
            mid=(end+start)/2;
            //找到了坏的的条件
            if (abs((start-end))<=1){ //ATT：这个地方请加abs，你他妈的
                break;
            }
            if (isBadVersion(mid)){
                end=mid; //现在这个是坏的就说明后面的都是坏的
            }
            else{
                start = mid; //坏的还没出现就移动start
            }
        }
        if(isBadVersion(start)){
            return start;
        }
        else if (isBadVersion(end)){
            return end;
        }
        else{
            return -1;
        }
    }
};