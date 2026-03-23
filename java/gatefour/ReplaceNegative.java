public class ReplaceNegative {
    public static int[] replaceNegatives(int[] arrays) {
        for (int index = 0; index < arrays.length; index++) {
            if (arrays[index] < 0) {
                arrays[index] = 0;
            }
        }
        return arrays;
    }

    public static void main(String[] args) {
        int[] input = {5, -9, 3, -6, 2, -11};
        int[] result = replaceNegatives(input);

        for (int numb : result) {
            System.out.print(numb + " ");
        }
    }
}
