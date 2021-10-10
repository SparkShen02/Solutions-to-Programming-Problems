import java.io.*;

public class taming {
    static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader(String file_name) throws IOException {
            din = new DataInputStream(new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public int nextInt() throws IOException {
            int ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');

            if (neg)
                return -ret;
            return ret;
        }

        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read() throws IOException {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }
    }
    public static void main(String[] args) throws IOException {
        Reader f = new Reader("taming.in");
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("taming.out")));

        int N = f.nextInt() + 1;
        int[] nums = new int[N];

        for (int i = 1; i < N; i++) {
            nums[i] = f.nextInt();
        }

        int[][][] dp = new int[N][N][N];
        if (nums[1] != 0) dp[1][1][0] = 1;

        int[][] minVal = new int[N][N];
        minVal[1][1] = dp[1][1][0];

        //k = 0: dp[i][j][k] = min(dp[i-1][j-1]) + (1 -> if k != 对应的数值)
        //k != 0: dp[i][j][k] = dp[i-1][j][k-1] + (1 -> if k != 对应的数值)
        for (int i = 2; i < N; i++) {
            for (int j = 1; j < N; j++) {
                int min = 101;
                for (int k = 0; j + k <= i ; k++) {
                    if (j == 1) k = i - 1;

                    if (k == 0){
                        dp[i][j][k] = minVal[i-1][j-1];
                        if (k != nums[i]) dp[i][j][k] += 1;
                    }
                    else{
                        dp[i][j][k] = dp[i-1][j][k-1];
                        if (k != nums[i]) dp[i][j][k] += 1;
                    }

                    min = Math.min(min, dp[i][j][k]);
                }
                minVal[i][j] = min;
            }
        }

        for (int j = 1; j < N; j++) {
            out.println(minVal[N-1][j]);
        }
        out.close();
    }
}
