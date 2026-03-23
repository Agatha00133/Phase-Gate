import java.util.Scanner;
public class TaskSix{
public static void main(String[] args){
Scanner input = new Scanner(System.in);
int width;
int length;
System.out.print("Enter the width of a rectangle ");
width = input.nextInt();

System.out.print ("Enter the length of a rectangle ");
length = input.nextInt();
int area = width * length;
System.out.println("The area of a rectangle is : " + area);
}
}
