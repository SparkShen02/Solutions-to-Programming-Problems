public class Solution {
    /**
     * @param n: the value from 1 - n
     * @param value: the value of coins
     * @param amount: the number of coins
     * @return: how many different value
     */
    public int backPackVIII(int n, int[] value, int[] amount){
        boolean[] knap = new boolean[n+1];
        knap[0]=true;
        int count=0;
        int[] times;
        int val;
        
        for (int item=0; item<value.length; item++){
                val=value[item];
                times=new int[n+1];
                for (int tar=value[item]; tar<=n; tar++){
                    if (knap[tar]==false && times[tar-val]<amount[item] && knap[tar-val]==true){
                        knap[tar]=true;
                        times[tar]=times[tar-val]+1;//times[tar]->在达到tar时已经将val(value[item])加了几次
                        count+=1;
                    }
                }
        }
        return count;
    }
}