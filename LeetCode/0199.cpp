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
    /*
    Apply level-order traversal (breadth-first search) and record the last node of each level. 
    Time complexity: O(n), Space complexity: O(n). 
    */
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans; 
        if (root == nullptr)
            return ans; 

        queue<TreeNode*> q; 
        q.push(root); 
        while (!q.empty()) {
            int n = q.size(); 
            for (int i = 0; i < n; i++) {
                TreeNode* cur = q.front();
                q.pop();  
                if (i == n-1)
                    ans.push_back(cur->val); 
                if (cur->left != nullptr)
                    q.push(cur->left); 
                if (cur->right != nullptr)
                    q.push(cur->right); 
            }
        }
        return ans; 
    }
};