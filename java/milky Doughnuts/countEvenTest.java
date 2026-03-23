import org.junit.jupiter.api.Test;


import static org.junit.jupiter.api.Assertions.assertEquals;


public class countEvensTest {

    @Test
    public void testMixedNumbers() {
        assertEquals(3, countEvens.CountEvens(new int[]{1, 2, 3, 4, 6}));
    }

    @Test
   public void testAllEven() {
        assertEquals(3, countEvens.CountEvens(new int[]{2, 4, 6}));
    }

    @Test
   public void testNoEven() {
        assertEquals(0, countEvens.CountEvens(new int[]{1, 3, 5}));
    }
}
