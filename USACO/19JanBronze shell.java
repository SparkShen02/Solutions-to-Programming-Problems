import java.io.*;
import java.util.*;

public class shell {
    public static void main(String[] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("shell.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("shell.out")));
        StringTokenizer st = new StringTokenizer(f.readLine());

        int num = Integer.parseInt(st.nextToken());
        String[] arr = new String[num];
        int max = 0;
        for (int i = 1; i <= 3; i++) {
            int res = 0;
            int pos = i;
            for (int j = 1; j <= num ; j++) {
                if (i==1) {
                    arr[j-1] = f.readLine();
                }
                st = new StringTokenizer(arr[j-1]);
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                if (pos == a) pos = b;
                else if (pos == b) pos = a;
                if (pos == c) res += 1;
            }
            max = Math.max(max, res);
        }
        out.println(max);
        out.close();
    }
}
