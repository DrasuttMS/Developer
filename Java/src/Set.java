import java.util.HashSet;

public class Set {
    public static void main(String[] args) {

        //Declaracion y creacion
        HashSet<String> names = new HashSet<>();
        var numbers = new HashSet<Integer>();

        //Tamaño

        System.out.println(names.size());

        //Añadir elementos

        names.add("Max");
        names.add("Salas");
        names.add("Castillo");
        names.add("mba.salas@gmail,com");
        System.out.println(names.size());


    }
}
