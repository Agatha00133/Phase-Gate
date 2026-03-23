public class countEvens {

    public static int CountEvens(int[] numbers) {
        int count = 0;

        for (int num : numbers) {
            if (num % 2 == 0) {
                count++;
            }
        }

        return count;
    }
}
