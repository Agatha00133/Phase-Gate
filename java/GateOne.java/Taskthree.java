import java.util.Scanner;
public class Taskthree{
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    System.out.print("Enter frist numbers");
    int numbers1 = input.nextInt();

    System.out.print("Enter second numbers");
    int numbers2 = input.nextInt();
    int sum = numbers1 + numbers2;
    System.out.println(numbers1 + numbers2);

}
}
