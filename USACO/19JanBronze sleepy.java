import java.io.*;
import java.util.*;

public class sleepy {
    public static void main(String[] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("sleepy.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("sleepy.out")));
        StringTokenizer st = new StringTokenizer(f.readLine());

        int num = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(f.readLine());
        int[] line = new int[num];
        for (int i = 0; i < num; i++) {
            line[i] = Integer.parseInt(st.nextToken());
        }
        int res = 0;
        for (int i = num-1; i > 0 ; i--) {
            if (line[i] <= line[i-1]){
                res = i;
                break;
            }
        }
        out.println(res);
        out.close();
    }
}