
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
//分治法解

class Solution {
private:
    int maxDepthNum_;
    
    
    int get_depth(TreeNode* node, int currDepth){
        
        if(!node){
            return currDepth;
        }
        
        currDepth++;     
        int depthLeft=get_depth(node->left, currDepth);
        int depthRight=get_depth(node->right, currDepth);
        
        return max(depthLeft,depthRight);
    }
    
public:
    
    
    int maxDepth(TreeNode* root) {
     
        return get_depth(root, 0);
    }
};