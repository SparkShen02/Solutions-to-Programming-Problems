class Solution {
public:
    /*
    Split as soon as a balanced string can be formed. 
    Time complexity: O(n), Space complexity: O(1). 
    */
    int balancedStringSplit(string s) {
        int numL = 0; 
        int numR = 0; 
        int ans = 0; 
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == 'L')
                numL += 1; 
            else
                numR += 1; 
            if (numL == numR) {
                ans += 1; 
                numL = 0; 
                numR = 0; 
            }
        }
        return ans; 
    }
};