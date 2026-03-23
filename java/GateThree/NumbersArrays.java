import java.util.Arrays;
public class NumberLength{
    public static void main(String[] args){

        int[] array = {2,3,4};
        int[] newArray = new int[2];
        newArray[0] = array[0];
        newArray[1] = array[1];
   
        System.out.println(Arrays.toString(addToArray(array)));

    
  
    }



    public static int[] addToArray(int[] array){
        int [] numbers = new int [5];
        for(int count = 0; count <= numbers.length-1 ;count++){
//            if(count <= 2){
//                 numbers[count] = array[count];
//            }else{
                numbers[count]= -1;
            
        }    
        return numbers;
    }

}
