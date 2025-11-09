import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw =new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n];
        for(int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(br.readLine());
        }

        // 산술평균
        double avg = (double) Arrays.stream(numbers).sum() / n;
        int rounded = (int) Math.round(avg);
        bw.write(String.valueOf(rounded));
        bw.newLine();

        // 중앙값
        Arrays.sort(numbers);
        int center = numbers[n/2];
        bw.write(String.valueOf(center));
        bw.newLine();

        // 최빈값
        Map<Integer, Integer> freq = new HashMap<>();
        int maxCount = 0;
        for (int num : numbers) {
            int count = freq.getOrDefault(num, 0) + 1;
            freq.put(num, count);
            if (count > maxCount) maxCount = count;
        }

        List<Integer> modeList = new ArrayList<>();
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            if (e.getValue() == maxCount) {
                modeList.add(e.getKey());
            }
    
        }

        Collections.sort(modeList);
        int mode = (modeList.size() > 1) ? modeList.get(1) : modeList.get(0);
        bw.write(String.valueOf(mode));
        bw.newLine();

        // 범위
        bw.write(String.valueOf(numbers[n-1] - numbers[0]));

        br.close();
        bw.flush();
        bw.close();
    } 
}
