public class Solution {
    /**
     * @param nums: an integer array and all positive numbers, no duplicates
     * @param target: An integer
     * @return: An integer
     */
    public int backPackVI(int[] nums, int target) {
        //不同于排列唯一的背包问题，这种不限制排序的背包问题需要按照列来考虑
        int[] knap = new int[target+1];
        knap[0]=1;
        for (int tar=0; tar<=target; tar++) {
            for (int item=0; item<nums.length; item++) {
                if(tar>=nums[item]){ knap[tar] = knap[tar] + knap[tar-nums[item]];}
            }
        }
        return knap[target];
    }
}