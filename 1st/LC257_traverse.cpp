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

//这个题的关键是每个path要通过左右子树是不是存在而终结，不是跟子树不存在就终结，这个需要返回最长那一只path

class Solution {
private:    
    int go_next_layer(TreeNode* root, string output, vector<string>& paths){
        if(!root){ //空字符
            return -1;
        }
        
        
        if(output.empty()){
            output.append(to_string(root->val)); 
        }
        else{
            output.append("->"+to_string(root->val));
        }
        
        if(!root->left && !root->right){
            paths.push_back(output);
        }
        
        
        
        if(root->left){      
            go_next_layer(root->left, output, paths);
        }
        if(root->right){
            go_next_layer(root->right, output, paths);
        }
        return -1;
    }
    
    
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        
        vector<string> paths;
        
        go_next_layer(root,"", paths);
        
        return paths;
        
    }
    
    
};