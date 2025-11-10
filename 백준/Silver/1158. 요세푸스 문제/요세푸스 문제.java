import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder("<");
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            q.offer(i);
        }

        int count = 0;
        while (!q.isEmpty()) {
            count++;

            if (count == k) {
                sb.append(String.valueOf(q.poll()));
            } else if (count % k == 0) {
                sb.append(", " + String.valueOf(q.poll()));
            } else {
                q.offer(q.poll());
            }
        }
        sb.append(">");

        System.out.println(sb.toString());
    } 
}


