import java.io.*;
import java.util.*;

public class Main {
    static int[][] graph;
    static int n;
    static int m;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            
            for (int j = 0; j < m; j++) {
                graph[i][j] = s.charAt(j) - '0';
            }
        }

        System.out.println(bfs(0, 0));
    }

    static int bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});

        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cx = cur[0];
            int cy = cur[1];

            if (cx == n-1 && cy == m - 1) {
                return graph[cx][cy];
            }

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (graph[nx][ny] == 1) {
                        graph[nx][ny] = graph[cx][cy] + 1;
                        q.offer(new int[]{nx, ny});
                    }
                }
            }
        }

        return -1;
    }
}


