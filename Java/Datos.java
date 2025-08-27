import java.util.Scanner;

public class Datos {
    public static void main(String[] args) {
        String nombre;
        int a1, a2;
        Scanner teclado  = new Scanner(System.in);
        System.out.println("Introduce tu Nombre: ");
        nombre = teclado.nextLine();
        System.out.println("Introduce año de Nacimiento y actual ");
        a1 = teclado.nextInt();
        a2 = teclado.nextInt();
        System.out.println("Te llamas " + nombre);
        System.out.println("y tienes " + (a2 - a1) + " Años");
    }
}