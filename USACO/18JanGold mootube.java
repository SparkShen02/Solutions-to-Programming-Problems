import java.io.*;
import java.util.*;

class Tuple {
    public int a, b;
    public Tuple(int a, int b) {
        this.a = a;
        this.b = b;
    }
}

public class mootube {
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

    public static int dfs(int v, int k, ArrayList<Tuple>[] matrix) {
        int result = 0;
        LinkedList<Integer> explore = new LinkedList<Integer>();
        // Set<Integer> visited = new HashSet<Integer>();
        boolean[] visited = new boolean[matrix.length];
        explore.add(v);

        while (!explore.isEmpty()) {
            int node = explore.remove();

            visited[node] = true;

            for (Tuple tup: matrix[node]) {
                int cost = tup.b;
                int u = tup.a;

                if (!visited[u] && cost>=k) {
                    explore.add(u);
                    result += 1;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        Reader f = new Reader("mootube.in");
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("mootube.out")));

        int n = f.nextInt();
        int q = f.nextInt();

        ArrayList<Tuple>[] matrix = new ArrayList[n];

        for(int i = 0; i < n-1; i++) {
            int a = f.nextInt()-1;
            int b = f.nextInt()-1;
            int cost = f.nextInt();
            if (matrix[a] == null) matrix[a] = new ArrayList<Tuple>();
            if (matrix[b] == null) matrix[b] = new ArrayList<Tuple>();
            matrix[a].add(new Tuple(b, cost));
            matrix[b].add(new Tuple(a, cost));
        }

        for(int j = 0; j < q; j++) {
            int k = f.nextInt();
            int v = f.nextInt()-1;
            out.println(dfs(v, k, matrix));
        }

        out.close();
    }
}