class Solution {
public:
    /*
    f_max[i] = the max product of any contiguous subarray that ends with nums[i]
    f_min[i] = the min product of any contiguous subarray that ends with nums[i]
    f_max[i] = max(nums[i], nums[i]*f_max[i-1], nums[i]*f_min[i-1])
    f_min[i] = min(nums[i], nums[i]*f_max[i-1], nums[i]*f_min[i-1])
    Time complexity: O(n), Space complexity: O(1). 
    */
    int maxProduct(vector<int>& nums) { 
        int curMax = nums[0]; // f_max[i]
        int curMin = nums[0]; // f_min[i]
        int ans = curMax; 
        for (int i = 1; i < nums.size(); i++) {
            int tempMax = max(nums[i], max(nums[i]*curMax, nums[i]*curMin)); 
            curMin = min(nums[i], min(nums[i]*curMax, nums[i]*curMin));
            curMax = tempMax; 
            ans = max(ans, curMax); 
        }
        return ans; 
    }
};