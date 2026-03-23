public class movesZeros {
    public static int[] moveZeros(int[] arrays) {
        int[] result = new int[arrays.length];
        int index = 0;

        
        for (int number : arrays) {
            if (number != 0) {
                result[index++] = number;
            }
        }

        
        return result;
    }

    public static void main(String[] args) {
        int[] input = {5, 0, 3, 0, 2, 0};
        int[] result = moveZeros(input);

        for (int number : result) {
            System.out.print(number + " ");
        }
    }
}
