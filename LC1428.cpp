/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *   public:
 *     int get(int row, int col);
 *     vector<int> dimensions();
 * };
 */

//这里还有一种更加快的linear time的解法。我们从matrix的右上角出发，首先往下走，如果遇到1的时候，我们就往左走。直到遇到0为止，我们继续往下走。这样的原因是因为每一行都是Non-decreasing的，我们假设最左边的1出现在第x行。通过我们的算法，我们一定会遇到第x行，因为在这之上所有行数最左边的1都会出现在第X行1的右边。当我们遇到第X行的时候，我们又会一直走到第X行的最右边。所以我们一定可以遍历到最早出现1的column.
//https://blog.csdn.net/MrJustin/article/details/105672624

class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        vector <int> dim = binaryMatrix.dimensions();
        int row = 0; int col = dim[1]-1; int res = dim[1];
        while(row<dim[0] && col>=0){
            if(binaryMatrix.get(row, col) == 0){
                row++;
            }else{
                res = col;
                col--;
            }
        }
        
        if(res == dim[1]) return -1;
        else return res;
    }
};