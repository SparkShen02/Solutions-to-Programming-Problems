class Solution {
public:
    /*
    Suppose a and b are the answers we want, xor all the numbers to get a^b. In a^b, find a bit that is 1. Then, traverse the array again, for each number, check if it is 1 at the bit we just found.
    This puts the array into two groups. In each group, there is one number that appears once, and other numbers all appear twice. 
    Time complexity: O(n), Space complexity: O(1).  
    */
    vector<int> singleNumbers(vector<int>& nums) {
        int aXb = 0;
        for (int i = 0; i < nums.size(); i++)
            aXb ^= nums[i];

        int bit = 1; 
        while (true)
        {
            if (aXb & bit)
                break;
            bit <<= 1; 
        }

        int a = 0;
        int b = 0; 
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] & bit)
                a ^= nums[i];
            else
                b ^= nums[i];
        }

        vector<int> ans;
        ans.push_back(a);
        ans.push_back(b);
        return ans; 
    }
};