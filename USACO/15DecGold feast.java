import java.io.*;
import java.util.*;

public class feast {
    static class Reader {
        final private int BUFFER_SIZE = 1 << 16; // line length, remember to adjust if necessary ! ! !
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
        Reader f = new Reader("feast.in");
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("feast.out")));
        int T = f.nextInt();
        int A = f.nextInt();
        int B = f.nextInt();

        boolean[][] s = new boolean[2][T+1];

        if (B<A) {
            int temp = B;
            B = A;
            A = temp;
        }

        s[0][0] = true;
        for (int t = 1; t <= T; t++) {
            if (t>=A) s[0][t] |= s[0][t-A];
            if (t>=B) s[0][t] |= s[0][t-B];
        }

        for (int t = 0; t <= T ; t++) {
            if (t>=A) s[1][t] |= s[1][t-A];
            if (t>=B) s[1][t] |= s[1][t-B];
            if (2*t<=T) s[1][t] |= s[0][2*t];
            if (2*t+1<=T) s[1][t] |= s[0][2*t+1];
        }

        for (int t=T; t>=0; t--){
            if (s[1][t] || s[0][t]) {
                out.println(t);
                break;
            }
        }

        out.close();
    }
}