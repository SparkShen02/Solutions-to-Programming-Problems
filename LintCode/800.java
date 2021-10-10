public class Solution {
    /**
     * @param n: Your money
     * @param prices: Cost of each university application
     * @param probability: Probability of getting the University's offer
     * @return: the  highest probability
     */
    public double backpackIX(int n, int[] prices, double[] probability) {
        //每所大学只能申请一次
        //pro=1-(1-knap[tar-prices[item]])*(1-probability[item])
        //knap[tar] = Math.max(knap[tar], pro)
        double[] knap=new double[n+1];
        double pro;
        
        for (int item=0; item<prices.length; item++){
            for (int tar=n; tar>=prices[item]; tar--){
                pro=1-(1-knap[tar-prices[item]])*(1-probability[item]);
                knap[tar] = Math.max(knap[tar], pro);
            }
        }
        
        return knap[n];
    }
}