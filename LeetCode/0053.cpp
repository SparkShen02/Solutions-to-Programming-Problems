class Solution {
public:
    /*
    f[i] represents the largest sum of any subarray that ends at position i. f[i] = max(f[i], nums[i] + f[i-1]). The largest of f[i] is the largest sum of any subarray. 
    Time complexity: O(n), Space complexity: O(1). 
    */
    int maxSubArray(vector<int>& nums) {
        int cur_f_i = nums[0]; // f[0] = nums[0]
        int max_f_i = cur_f_i; 
        for (int i = 1; i < nums.size(); i++)
        {
            cur_f_i = max(nums[i], nums[i] + cur_f_i); 
            if (cur_f_i > max_f_i)
                max_f_i = cur_f_i; 
        }
        return max_f_i; 
    }
};
