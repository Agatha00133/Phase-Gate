import java.util.*;

public class Main {
    public static List<Integer> findDuplicates(int[] arrays) {
        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new LinkedHashSet<>();

        for (int numb : arrays) {
            if (seen.contains(numb)) {
                duplicates.add(numb);
            } else {
                seen.add(numb);
            }
        }

        return new ArrayList<>(duplicates);
    }

    public static void main(String[] args) {
        int[] input = {45, 60, 3, 0, 67, 2, 45, 3, 22, 0};
        System.out.println(findDuplicates(input)); 
    }
}
