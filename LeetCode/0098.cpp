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
public:
    long last = LONG_MIN; // stores the value of the last visited node

    bool inorder(TreeNode* node) {
        if (node == nullptr)
            return true;

        if (!inorder(node->left))
            return false;
        if (node->val <= last) // not in sorted order
            return false; 
        last = node->val; 
        if (!inorder(node->right))
            return false;
        return true; 
    }

    /*
    A binary tree is a valid BST if its in-order traversal visits the nodes in a sorted order. 
    Time complexity: O(n), Space complexity: O(height). 
    */
    bool isValidBST(TreeNode* root) {
        return inorder(root); 
    }
};