/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
/* 分治法
左子树是平衡二叉树
右子树是平衡二叉树
左右子树高不超过1 

多写一个类来表示TF和高度，这样返回两个值
*/
//  多写一个结果类
class ResPack {
    public:
        bool res_;
        int depth_;
    
        ResPack(bool res, int depth){
            this->res_=res;
            this->depth_=depth;
        }
};


class Solution {
private:
    
    ResPack helper(TreeNode* node){
        if(!node){
            return ResPack(true, 0);
        }
        
        ResPack left=helper(node->left);
        ResPack right=helper(node->right);
        
        //左右子树任意一个不平衡即不平衡
        if(!left.res_ || !right.res_){
            return ResPack(false, -1);
        }
        
        //本身自己是不是平衡树
        if(abs(left.depth_-right.depth_) >1){
            return ResPack(false, -1);
        }
        
        return ResPack(true, max(left.depth_, right.depth_)+1);
        
    }
    
public:
    bool isBalanced(TreeNode* root) {
        return helper(root).res_;
    }
};