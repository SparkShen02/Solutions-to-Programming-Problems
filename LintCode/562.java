public class Solution {
    /**
     * @param nums: an integer array and all positive numbers, no duplicates
     * @param target: An integer
     * @return: An integer
     */
    public int backPackIV(int[] nums, int target) {
        //knap[i][n]->从前i种物品中，组成总和为n的可能组合的总数
        int[] knap = new int[target+1];
        knap[0]=1;
        
        for (int item=0; item<nums.length; item++){
            for (int tar=nums[item]; tar<=target; tar++){
                knap[tar] = knap[tar] + knap[tar-nums[item]];
            }
        }
        
        return knap[target];
    }
}