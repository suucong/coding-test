import java.io.*;
import java.util.*;

public class Main {
    static boolean[] visited;
    static ArrayList<Integer>[] graph;
    static StringBuffer sb;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());
        
        visited = new boolean[n+1];
        graph = new ArrayList[n+1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 0; i <= n; i++) {
            Collections.sort(graph[i]);
        }

        sb = new StringBuffer();
        dfs(v);

        sb.append("\n");
        Arrays.fill(visited, false);

        bfs(v);

        System.out.println(sb.toString());
    } 

    static void dfs(int x) {
        visited[x] = true;
        sb.append(x + " ");

        for (int next : graph[x]) {
            if (!visited[next]) dfs(next);
        }
    }

    static void bfs(int x) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(x);

        visited[x] = true;

        while (!q.isEmpty()) {
            int cur = q.poll();
            sb.append(cur + " ");

            for (int next : graph[cur]) {
                if (!visited[next]) {
                    visited[next] = true;
                    q.offer(next);
                }
            }
        }
    }
}


