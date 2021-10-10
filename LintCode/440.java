public class Solution {
    /**
     * @param A: an integer array
     * @param V: an integer array
     * @param m: An integer
     * @return: an array
     */
    public int backPackIII(int[] A, int[] V, int m) {
        int[] knap=new int[m+1];
        for (int item=0; item<A.length; item++){
            for (int val=A[item]; val<=m; val++){
                knap[val]=Math.max(knap[val], knap[val-A[item]]+V[item]);
            }
        }
        return knap[m];
    }
}