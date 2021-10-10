public class Solution {
    /*
     * @param A: An integer array
     * @param target: An integer
     * @return: An integer
     */
    public int MinAdjustmentCost(List<Integer> A,int target){
        int[][] minCost=new int[A.size()][101];//minCost[a][b]->前a个数字，并把A[a]设为b的最小cost
        
        for(int i=0;i<A.size();i++){
            for(int num=1;num<=100;num++){
                if(i==0){minCost[i][num]=Math.abs(num-A.get(i));}
                else{
                    
                    minCost[i][num]=Integer.MAX_VALUE;
                    int up=Math.min(num+target,100);
                    int down=Math.max(num-target,1);
                    for(int k=down;k<=up;k++){
                        minCost[i][num]=Math.min(minCost[i][num],minCost[i-1][k]+Math.abs(num-A.get(i)));
                    }
                    
                }
            }
        }
        
        int mini=Integer.MAX_VALUE;
        for(int i=1;i<=100;i++){
            mini=Math.min(mini,minCost[minCost.length-1][i]);
        }
        return mini;
    }
}