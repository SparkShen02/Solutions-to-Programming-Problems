import java.io.*;
import java.util.*;

public class snakes {
    public static int K;
    public static int N;
    public static int[] arr;
    public static int[][] cache;
    public static boolean[][] cache_bool;

    public static int dp_recur(int i, int j, int N, int[] arr) {
        //System.out.print(i);

        if (cache_bool[i][j]){
            return cache[i][j];
        }

        if (i == arr.length){
            return 0;
        }
        if (j == 0){
            return 999999999;
        }

        int res = 999999999;
        int last_cur = 0;
        int last_waste = 0;
        int cur = arr[i];

        for (int k=i; k<arr.length; k++){
            cur = Math.max(cur, arr[k]);
            int min_waste = last_waste + (cur-last_cur) * (k - i) + cur - arr[k];

            int cur_res = min_waste + dp_recur(k + 1, j - 1, N, arr);
            res = Math.min(res, cur_res);

            last_cur = cur;
            last_waste = min_waste;
        }

        cache_bool[i][j] = true;
        cache[i][j] = res;
        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("snakes.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("snakes.out")));
        StringTokenizer st = new StringTokenizer(f.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[N];

        st = new StringTokenizer(f.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        cache = new int[N+1][K+2];
        cache_bool = new boolean[N+1][K+2];

        //System.out.println(dp_recur(0, K+1, N, arr));
        out.println(dp_recur(0, K+1, N, arr));
        out.close();
    }
}