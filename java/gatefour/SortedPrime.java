import java.util.*;

public class SortedPrime {

    public static boolean isPrime(int value) {
        if (value < 2) return false;
        for (int index = 2; index <= Math.sqrt(value); index++) {
            if (value % index == 0) return false;
        }
        return true;
    }

    public static List<Integer> getSortedPrimes(int[] arrays) {
        List<Integer> primes = new ArrayList<>();

        for (int num : arrays) {
            if (isPrime(num)) {
                primes.add(num);
            }
        }

        
        Collections.sort(primes, Collections.reverseOrder());
        return primes;
    }

    public static void main(String[] args) {
        int[] input = {5, 9, 3, 6, 2};
        System.out.println(getSortedPrimes(input)); 
    }
}
