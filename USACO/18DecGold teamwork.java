import java.io.*;

public class teamwork {
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
        Reader f = new Reader("teamwork.in");
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("teamwork.out")));

        int N = f.nextInt();
        int K = f.nextInt();

        int[] nums = new int[N+1];
        for (int i = 1; i <= N; i++) {
            nums[i] = f.nextInt();
        }

        int[][] dp = new int[N+1][K+1];

        dp[1][1] = nums[1];
        int[]maxInRow = new int[N+1];

        for (int i = 2; i <= N ; i++) {
            int maxNum = 0;
            int maxRow = 0;
            for (int j = 1; j <= K ; j++) {
                if (j > i) break;
                maxNum = Math.max(maxNum, nums[i-j+1]);

                dp[i][j] = maxInRow[i-j] + j*maxNum;
                maxRow = Math.max(dp[i][j], maxRow);
            }
            maxInRow[i] = maxRow;
        }

        out.println(maxInRow[maxInRow.length-1]);
        out.close();
    }
}
