public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @param V: Given n items with value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int[] V) {
        int[] knap=new int[m+1];
        for(int num=0; num<A.length; num++){
            for(int cap=m; cap>=A[num]; cap--){
                knap[cap]=Math.max(knap[cap],knap[cap-A[num]]+V[num]);
            }
        }
        return knap[knap.length-1];
    }
}