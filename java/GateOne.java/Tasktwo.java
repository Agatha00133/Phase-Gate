import java.util.Scanner;
public class TaskTwo{
public static void main(String[] args){
Scanner input = new Scanner(System.in);
System.out.print("Enter your age ");
int age = input.nextInt();
int agecolletor = age + 5;
System.out.print("your age in five years time will be !: " + agecolletor + age);
}
}
