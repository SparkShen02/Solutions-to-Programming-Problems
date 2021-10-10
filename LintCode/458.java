public class Solution {
    /**
     * @param nums: An integer array sorted in ascending order
     * @param target: An integer
     * @return: An integer
     */
    public int lastPosition(int[] nums, int target) {
        int start=0;
        int end=nums.length-1;
        int mid;
        
        while (start<=end){
            mid=(start+end)/2;
            if (target>nums[mid]){ start=mid+1; }
            else if (target<nums[mid]){ end=mid-1; }
            else if (mid<nums.length-1 && nums[mid+1]==target){
                start=mid+1;
            }
            else{
                return mid; 
            }
        }
        
        return -1;
    }
}