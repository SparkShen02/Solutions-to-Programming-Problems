class Solution {
public:
    /*
    Start at the top-right corner: move left if target < curNum (because the whole column can be omitted), and move down if target > curNum (because the whole row can be omitted). Repeat until reach the bound.
    Time complexity: O(m+n), Space complexity: O(1). Explanation: Think about the search path, its length can be at most m+n. 
    */
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        int numR = matrix.size();

        if (numR == 0)
            return false;

        int curR = 0, curC = matrix[0].size() - 1; 
        while (curR < numR && curC >= 0) {
            int curNum = matrix[curR][curC]; 
            if (target == curNum)
                return true;
            else if (target < curNum)
                curC -= 1; // move left
            else
                curR += 1; // move down
        }
        return false; 
    }
};