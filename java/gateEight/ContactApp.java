import java.util.Scanner;
import java.util.ArrayList;
    public class ContactApp{
    
    static ArrayList<String> contacts = new ArrayList<>();
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args){

    System.out.print("=====welcome To ContactApp===== ");    
    System.out.println("\n1.Add contact needs : ");
    System.out.println("2. Remove contact : ");
    System.out.println("3. Find contact by phone : ");
    System.out.println("4. find contact by first name : ");
    System.out.println("5. find contact by last name : ");
    System.out.println("6. Edit contact : ");

     System.out.print("Choose option: ");
     int choice = input.nextInt();
     input.nextLine();

        if (choice == 1) {
            ContactAppAddcontactNeeds();
        } else if (choice == 2) {
            ContactAppRemoveContact();
        } else {
            System.out.println("Invalid option!");
        }
    }

    
    public static void ContactAppAddcontactNeeds(){
    System.out.print("Enter First Name : ");
    String firstName = input.nextLine();

    System.out.print("Enter Last Name : ");
    String lastName = input.nextLine();

    System.out.print("Enter phone Number : ");
    String phoneNumber = input.nextLine();

    String contact = firstName + " " + lastName + " - " + phoneNumber;
    contacts.add(contact);

    System.out.println("contact added successfully!");
}
 
    public static void ContactAppRemoveContact(){
    System.out.print("Enter PhoneNumber to delete: ");
    String phoneNumber = input.nextLine();
    
            boolean found = false;

        for (int i = 0; i < contacts.size(); i++) {
            if (contacts.get(i).contains(phoneNumber)) {
                contacts.remove(i);
                found = true;
                break;
            }
        }

        if (found) {
            System.out.println("contact removed successfully!");
            }else{
System.out.print("cont not found ! ");
    }
    }
}

