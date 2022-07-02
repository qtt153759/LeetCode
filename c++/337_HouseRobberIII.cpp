#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {}
        TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    };
    unordered_map<TreeNode*,int>umap;
    int rob(TreeNode* root) {
        if(root==NULL){
            return 0;
        }else if(umap[root]){
            return umap[root];
        }
        int max_l=0;
        int max_r=0;
        if(root->left!=NULL){
            max_l= rob(root->left->left)+rob(root->left->right);
        }
        if(root->right!=NULL){
            max_r=rob(root->right->left)+rob(root->right->right);
        }
        
        return umap[root]=max(root->val+max_l+max_r,rob(root->left)+rob(root->right));
    }
};
int main();