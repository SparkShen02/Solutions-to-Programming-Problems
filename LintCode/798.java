public class Solution {
    /**
     * @param n: the money of you
     * @param prices: the price of rice[i]
     * @param weight: the weight of rice[i]
     * @param amounts: the amount of rice[i]
     * @return: the maximum weight
     */
    public int backPackVII(int n, int[] prices, int[] weight, int[] amounts) {
        ArrayList<Integer> pri = new ArrayList();
        ArrayList<Integer> wei=new ArrayList();
        for (int a=0; a<amounts.length; a++){
            for (int b=0; b<amounts[a]; b++){
                pri.add(prices[a]);
                wei.add(weight[a]);
            }
        }

        int[] knap=new int[n+1];
        for(int num=0; num<pri.size(); num++){
            for(int cap=n; cap>=pri.get(num); cap--){
                knap[cap]=Math.max(knap[cap], knap[cap-pri.get(num)]+wei.get(num));
            }
        }
        return knap[knap.length-1]; 
    }
}