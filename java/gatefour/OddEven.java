import java.util.*;

public class OddEven {
    public static List<List<Integer>> splitEvenOdd(int[] arrays) {
        List<Integer> odd = new ArrayList<>();
        List<Integer> even = new ArrayList<>();

        for (int number : arrays) {
            if (number % 2 != 0) {
                odd.add(number);
            } else {
                even.add(number);
            }
        }

        List<List<Integer>> result = new ArrayList<>();
        result.add(odd);
        result.add(even);

        return result;
    }

    public static void main(String[] args) {
        int[] input = {45, 60, 3, 10, 9, 22};
        System.out.println(splitEvenOdd(input)); 
    }
}
