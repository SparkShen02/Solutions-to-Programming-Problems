class Solution {
public:
    /*
    Use a variable n to store the last index of the transformed array. 
    Traverse nums. If a new number is found, insert it at nums[n+1]. 
    Time complexity: O(n), Space complexity: O(1). 
    */
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) 
            return 0; 

        int n = 0;  
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[n]) {
                nums[n+1] = nums[i]; 
                n += 1;
            }
        }
        return n + 1; 
    }
};
