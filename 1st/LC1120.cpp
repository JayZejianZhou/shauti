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

class ResPack{
public:
    int sum_;
    int nodeNum_;
    
    ResPack(int sum, int nodeNum){
        this->sum_=sum;
        this->nodeNum_=nodeNum;
    }
};

class Solution {
private:
    double maxAve=0;
    
    
    ResPack helper(TreeNode* node){
        if(!node){
            return ResPack(0,0);
        }
        
        ResPack left=helper(node->left);
        ResPack right=helper(node->right);
        
        double avg=(left.sum_+right.sum_+node->val)/double(left.nodeNum_+right.nodeNum_+1);
        
        this->maxAve=max(this->maxAve, avg);
        
        return ResPack(left.sum_+right.sum_+node->val, left.nodeNum_+right.nodeNum_+1);
        
    }
    
public:
    double maximumAverageSubtree(TreeNode* root) {
        helper(root);
        return this->maxAve;
    }
};