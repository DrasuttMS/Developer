public class Conditionals {
    public static void main(String[] args) {

        //condicionales

        var age = 32;

        if (age > 18) {
            System.out.println("El usuario es mayor de edad");
        } else if (age == 18) {
            System.out.println("El usuario acaba de cumplir 18 años");
        } else {
            System.out.println("El usuario es menor de edad");
        }

        // switch

        var day = 1;
        switch (day){
            case 1:
                System.out.println("lunes");
                break;
            case 2:
                System.out.println("martes");
                break;
            case 3:
                System.out.println("miercoles");
                break;
            default:
                System.out.println("Otro dia");
        }
    }
}
