class Solution {
public:
    /*
    0 -->     0  --> 0
    1 -->     1  --> 1
    2 -->    10  --> 1
    3 -->    11  --> 2
    4 -->   100  --> 1
    5 -->   101  --> 2
    6 -->   110  --> 2
    7 -->   111  --> 3
    8 -->  1000  --> 1
    9 -->  1001  --> 2
    Let n be the largest power of 2 (1, 2, 4, 8, ...) such that n < i. 
    ans[n] = 1. ans[i] = ans[n] + ans[i-n] = 1 + ans[i-n].
    Time complexity: O(n), Space complexity: O(n) (the resulting list/vector).
    */
    vector<int> countBits(int n) {
        vector<int> ans(n+1);
        ans[0] = 0;
        int lastMultOfTwo;
        int nextMultOfTwo = 1; 
        for (int i = 1; i < n+1; i++) {
            if (i == nextMultOfTwo) {
                ans[i] = 1;
                lastMultOfTwo = nextMultOfTwo;
                nextMultOfTwo *= 2; 
            }
            else
                ans[i] = 1 + ans[i-lastMultOfTwo];
        }
        return ans;
    }
};