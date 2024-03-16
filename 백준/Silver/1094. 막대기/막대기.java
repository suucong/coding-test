import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<Integer, Integer> hs = new HashMap<>();
        hs.put(64, 1);
        int sum = 64, smallest = 64;
        int x = scanner.nextInt();
        while(sum > x) {
            if(hs.getOrDefault(smallest, 1) > 1) hs.put(smallest, hs.get(smallest)-1);
            else hs.remove(smallest);
            hs.put(smallest/2, 2);
            smallest = smallest/2;
            if((sum - smallest) >= x) {
                hs.put(smallest, 1);
                sum -= smallest;
            }
        }

        System.out.println(hs.keySet().size());
    }
}