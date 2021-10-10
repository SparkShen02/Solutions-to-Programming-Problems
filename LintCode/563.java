public class Solution {
    /**
     * @param nums: an integer array and all positive numbers
     * @param target: An integer
     * @return: An integer
     */
    public int backPackV(int[] nums, int target) {
        //knap[i][n]->从前i种物品中，组成总和为n的可能组合的总数
        int[] knap=new int[target+1];
        for (int i=0; i<knap.length; i++){knap[i]=0;}
        knap[0]=1;
        for (int item=0; item<nums.length; item++){
            for (int tar=target; tar>=nums[item]; tar--){
                knap[tar] = knap[tar] + knap[tar-nums[item]];
            }
        }
        return knap[knap.length-1];
    }
}