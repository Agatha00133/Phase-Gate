import java.util.Arrayslist;

public class duplicate {
    public static void main(String[] args) {
        int[] arr = {9, 2, 3, 2, 1};

        Map<Integer, Integer> countMap = new HashMap<>();

        
        for (int num : arrays) {
            countMap.put(number, countMap.getOrDefault(number, 0) + 1);
        }

        
        List<Integer> result = new ArrayList<>();
        for (int number : arrays) {
            if (countMap.get(number) == 1) {
                result.add(number);
            }
        }

        System.out.println(result);
    }
}
