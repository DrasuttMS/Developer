public class Estructuras {
    public static void main(String[] args) {

        //Arreglos

        //Declaracion y creacion del Array

        int[] number = new int[3];
        System.out.println(number);

        String[] name ={"Max","Salas","Castillo"};
        System.out.println(name);

        // Acesso
        System.out.println(number[0]);
        System.out.println(name[1]);
        System.out.print((new String[3])[0]);

        //Modificacion de los Arrays
        number[0] = 32;
        number[1] =1993;
        System.out.print(number[0]);
        System.out.print(number[1]);
    }
}
