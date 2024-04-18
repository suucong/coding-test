import java.util.Arrays;
import java.util.Objects;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 입력
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String[] list = new String[n];
        for (int i = 0; i < n; i++) list[i] = scanner.next();

        // 구현
        list = Arrays.stream(list).distinct().toArray(String[]::new);   // 중복 제거
        int j;
        for (int i = 1; i < list.length; i++) {
            String target = list[i];
            for (j = i - 1; j >= 0; j--) {
                if (target.length() < list[j].length()) {
                    list[j + 1] = list[j];
                } else if (target.length() == list[j].length()) {
                    if (target.compareTo(list[j]) < 0)  list[j + 1] = list[j];
                    else break;
                } else break;
            }
            list[j + 1] = target;
        }

        // 출력
        for (String str : list) if (!Objects.equals(str, ""))  System.out.println(str);
    }
}