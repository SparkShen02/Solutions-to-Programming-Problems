import java.io.*;
import java.util.*;

public class template2 {
    public static void main(String[] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("xxx.in"));
        // BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("xxx.out")));
        StringTokenizer st = new StringTokenizer(f.readLine());

        int num = Integer.parseInt(st.nextToken());

        out.println();
        out.close();
    }
}