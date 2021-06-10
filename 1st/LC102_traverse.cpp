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
    vector<vector<int>> res_;
    
    int go_next_layer(TreeNode* node, int currDepth){ 
        
        //corner case, empty tree
        if(!node){
            return -1;
        }        
        
        //动态添加结果数组尺寸
        if(this->res_.size()==currDepth){
            this->res_.push_back({});
        }

        this->res_[currDepth].push_back(node->val);     
        
        
        if(node->left){
            go_next_layer(node->left, currDepth+1);
        }
        if(node->right){
            go_next_layer(node->right, currDepth+1);
        }
        
        return -1;
    }
    
    
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        //corner case, empty tree
        if(!root){
            return this->res_;
        }

        go_next_layer(root, 0);

        return this->res_;
    }
};