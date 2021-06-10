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
class Solution {
private:
    int maxDepthNum=0;
    
    int go_next_layer(TreeNode* root, int depth){
        if(!root){
            this->maxDepthNum=max(depth, this->maxDepthNum);
            return -1;
        }
        else{
            depth++;
            go_next_layer(root->left, depth); // 前序遍历
            go_next_layer(root->right, depth);
        }
        return-1;
    }
    
public:
    
    int maxDepth(TreeNode* root) {
        this->maxDepthNum=0;
        
        go_next_layer(root,0);
        return this->maxDepthNum;
    }
    
    
};