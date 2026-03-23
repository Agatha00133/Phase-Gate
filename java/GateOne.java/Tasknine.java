import java.util.Scanner;
public class Tasknine{
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter the ItemPrice ");
    double  ItemPrice = input.nextDouble();
    double tax = 0.1;
    double total = ItemPrice + tax;
    System.out.println(total);  
    }
}
    

    
