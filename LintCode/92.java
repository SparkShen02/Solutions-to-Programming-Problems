public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    public int backPack(int m, int[] A) {
        int[] knap=new int[m+1];
        for(int i=0;i<A.length;i++){
            for(int c=m;c>=A[i];c--){
                knap[c]=Math.max(knap[c],knap[c-A[i]]+A[i]);
            }
        }
        return knap[knap.length-1];
    }
}