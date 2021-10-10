import java.io.*;
import java.util.*;

class Pair {
    public int a, b;
    public Pair (int a, int b) {
        this.a = a;
        this.b = b;
    }
}

public class perimeter {
    static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public Reader(String file_name) throws IOException {
            din = new DataInputStream(new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public String readLine() throws IOException {
            byte[] buf = new byte[1000]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n')
                    break;
                buf[cnt++] = (byte) c;
            }
            return new String(buf, 0, cnt);
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
        Reader f = new Reader("perimeter.in");
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("perimeter.out")));

        int num = f.nextInt();
        String[] matrix = new String[num];
        for (int i = 0; i < num; i++) {
            matrix[i] = f.readLine();
        }

        boolean[][] visited = new boolean[num][num];
        int max_area = 0;
        int max_peri = 0;
        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                if (matrix[i].substring(j, j+1).equals(".")) continue;

                LinkedList<Pair> toVisit = new LinkedList<>();
                toVisit.add(new Pair(i, j));
                int area = 0;
                int peri = 0;

                while (!toVisit.isEmpty()){
                    Pair cur = toVisit.remove();
                    int row = cur.a;
                    int col = cur.b;
                    if (visited[row][col]) continue;

                    int minus = 0;
                    area += 1;
                    visited[row][col] = true;

                    int[][] positions = {{row-1, col}, {row+1, col}, {row, col-1}, {row, col+1}};
                    for (int[] arr: positions) {
                        int newRow = arr[0];
                        int newCol = arr[1];
                        if ((0<=newRow) && (newRow<num) && (0<=newCol) && (newCol<num) && (matrix[newRow].substring(newCol, newCol+1).equals("#"))){
                            minus += 1;
                            if (!visited[newRow][newCol]) toVisit.add(new Pair(newRow, newCol));
                        }
                    }
                    peri += 4 - minus;
                }
                if (max_area < area) {
                    max_area = area;
                    max_peri = peri;
                }
                else if(max_area == area){
                    max_peri = Math.min(peri, max_peri);
                }
            }
        }

        out.println(max_area + " " + max_peri);
        out.close();
    }
}