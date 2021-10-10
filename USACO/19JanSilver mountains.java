import java.io.*;
import java.util.*;

class mountain implements Comparable<mountain>{
    public int verticeX, verticeY, leftX, rightX;
    public mountain(int verticeX, int verticeY) {
        this.verticeX = verticeX;
        this.verticeY = verticeY;
        this.leftX = verticeX - verticeY;
        this.rightX = verticeX + verticeY;
    }
    public int compareTo(mountain b) {
        return this.leftX - b.leftX;
    }

}
public class mountains {
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
            while (c <= ' ') {
                c = read();
            }
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
        Reader f = new Reader("mountains.in");
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("mountains.out")));

        int num = f.nextInt();
        mountain[] mountains = new mountain[num];
        for (int i = 0; i < num ; i++) {
            int x = f.nextInt();
            int y = f.nextInt();
            mountains[i] = new mountain(x, y);
        }

        Arrays.sort(mountains);

        int shown = 0;
        int left = -10000000;
        int right = -10000000;
        for (int i = 0; i < num ; i++) {
            mountain cur = mountains[i];
            if((cur.leftX == left) && (cur.rightX > right))  right = cur.rightX;
            else if (cur.rightX > right){
                shown += 1;
                left = cur.leftX;
                right = cur.rightX;
            }
        }
        out.println(shown);
        out.close();
    }
}