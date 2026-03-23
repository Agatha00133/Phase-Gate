public class PalindromicArray {
    public static boolean isPalindromic(int[] array) {
        int left = 0;
        int right = array.length - 1;

        while (left < right) {
            if (array[left] != array[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 2, 1};
        System.out.println(isPalindromic(array));
    }
}
