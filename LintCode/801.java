public class Solution {
    /**
     * @param n: the money you have
     * @return: the minimum money you have to give
     */
    public int backPackX(int n) {
        int[] nums={150,250,350};
        int[] dp=new int[1 + n];
        for (int i = 0; i < 3; i++) {
            for (int tar=nums[i]; tar<=n; tar++)
                dp[tar] = Math.max(dp[tar], dp[tar - nums[i]]+nums[i]);
        }
        return n-dp[n];
    }
}