import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] word = br.readLine().toUpperCase().toCharArray();

        Map<Character, Integer> freq = new HashMap<>();
        int maxCount = 0;
        for (char c : word) {
            int count = freq.getOrDefault(c, 0) + 1;
            freq.put(c, count);
            if (count > maxCount) maxCount = count;
        }

        List<Character> maxList = new ArrayList<>();
        for (Map.Entry<Character, Integer> e : freq.entrySet()) {
            if (e.getValue() == maxCount) {
                maxList.add(e.getKey());
            }
        }

        if (maxList.size() == 1) {
            System.out.println(String.valueOf(maxList.get(0)));
        } else {
            System.out.println("?");
        }
    } 
}


