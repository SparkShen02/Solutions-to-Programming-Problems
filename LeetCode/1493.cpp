class Solution {
public:
    /*
    Maintain a sliding window where there is at most one zero in it. 
    Time complexity: O(n), Space complexity: O(1). 
    */
    int longestSubarray(vector<int>& nums) {
        int l = 0, r = 0;
        int maxAns = 0; 
        while (1) {
            bool containsZero = nums[l] == 0;
            while (r+1 < nums.size()) {
                if (nums[r+1] == 1)
                    r += 1;
                else {
                    if (containsZero)
                        break; 
                    else {
                        containsZero = true; 
                        r += 1; 
                    }
                }
            }

            maxAns = max(maxAns, r-l);
            if (r+1 == nums.size())
                return maxAns;
            
            while (nums[l] == 1)
                l += 1;
            if (l == r) {
                l += 1; 
                r += 1; 
            }
            else
                l += 1; 
        }
    }
};