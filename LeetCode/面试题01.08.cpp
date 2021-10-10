class Solution {
public:
    /*
    Use two variables to record whether the first row contains 0 and whether the first column contains 0. 
    Then, use the first row to record whether a certain column contains 0 and the first column to record whether a certain row contains 0. 
    Time complexity: O(MN), Space complexity: O(1). 
    */
    void setZeroes(vector<vector<int>>& matrix) {
        int M = matrix.size(); 
        int N = matrix[0].size(); 

        bool firstRowHasZero = false; 
        for (int c = 0; c < N; c++) {
            if (matrix[0][c] == 0) {
                firstRowHasZero = true; 
                break; 
            }
        }
        bool firstColHasZero = false; 
        for (int r = 0; r < M; r++) {
            if (matrix[r][0] == 0) {
                firstColHasZero = true; 
                break; 
            }
        }

        for (int r = 1; r < M; r++) {
            for (int c = 1; c < N; c++) {
                if (matrix[r][c] == 0) {
                    matrix[0][c] = 0; 
                    matrix[r][0] = 0; 
                }
            }
        }

        for (int r = 1; r < M; r++) {
            for (int c = 1; c < N; c++) {
                if (matrix[0][c] == 0 || matrix[r][0] == 0)
                    matrix[r][c] = 0; 
            }
        }

        if (firstRowHasZero) {
            for (int c = 0; c < N; c++)
                matrix[0][c] = 0; 
        }
        if (firstColHasZero) {
            for (int r = 0; r < M; r++)
                matrix[r][0] = 0; 
        }
    }
};