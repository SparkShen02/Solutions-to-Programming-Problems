import java.io.*;
import java.util.*;

public class guess {
    public static void main(String[] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("guess.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("guess.out")));
        StringTokenizer st = new StringTokenizer(f.readLine());

        int num = Integer.parseInt(st.nextToken());
        ArrayList<String[]> arr = new ArrayList<>();
        for (int i = 0; i < num; i++) {
            st = new StringTokenizer(f.readLine());
            st.nextToken();
            int n= Integer.parseInt(st.nextToken());
            String[] line = new String[n];
            for (int j = 0; j < n; j++) {
                line[j] = st.nextToken();
            }
            arr.add(line);
        }

        int res = 0;
        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                if (i == j) continue;
                int cur = 0;
                for (String ch : arr.get(j)) {
                    if (Arrays.asList(arr.get(i)).contains(ch)) cur += 1;
                }
                res = Math.max(res, cur);
            }
        }

        out.println(res+1);
        out.close();
    }
}