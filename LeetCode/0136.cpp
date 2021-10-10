class Solution {
public:
    /*
    Use the xor boolean algebra. a^a = 0, a^0 = a. 
    Suppose nums = [a, b, c, d, b, c, a]. a^b^c^d^b^c^a = (a^a) ^ (b^b) ^ (c^c) ^ d = 0^0^0^d = d. 
    Time complexity: O(n), Space complexity: O(1). 
    */
    int singleNumber(vector<int>& nums) {
        int ans = 0; 
        for (int i = 0; i < nums.size(); i++)
            ans = ans^nums[i];
        return ans; 
    }
};