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
    int currMinDepth_;
    
    int go_next_layer(TreeNode* node, int depth){
        
        //corner case
        if(!node){
            this->currMinDepth_=0;
            return -1;
        }
        
        
        depth++;
        
        
        
        if(!node->left && !node->right){
            if(this->currMinDepth_ <= depth){ //查看是否现在的深度是最小的
                return -1;
            }
            else{
                this->currMinDepth_ = depth; 
                return -1;
            }
        }    
        
        //前序遍历，递归
        if(node->left){
            go_next_layer(node->left, depth);
        }
        if(node->right){
            go_next_layer(node->right, depth);
        }
        
        return -1;
    }
    
public:
    int minDepth(TreeNode* root) {
        this->currMinDepth_=99999;
        go_next_layer(root, 0);
        return this->currMinDepth_;
    }
};