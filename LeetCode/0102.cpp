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
    Breadth first search. Record answers seperately for each level. 
    Time complexity: O(n), Space complexity: O(n). 
    */
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (root == nullptr)
            return ans; 
            
        std::queue<TreeNode*> q; 
        q.push(root); 
        while (!q.empty()) {
            vector<int> curLevelAns; 
            int n = q.size(); // # of nodes at current level

            for (int i = 0; i < n; i++) {
                TreeNode* cur = q.front(); 
                q.pop(); 
                curLevelAns.push_back(cur->val); 
                if (cur->left != nullptr)
                    q.push(cur->left); 
                if (cur->right != nullptr)
                    q.push(cur->right); 
            }

            ans.push_back(curLevelAns);
        }
        return ans; 
    }
};