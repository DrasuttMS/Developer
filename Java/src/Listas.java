import java.util.ArrayList;

public class Listas {
    public static void main(String[] args) {
        //Listas
        //Declaracion y creacion
        ArrayList<String> names = new ArrayList<>();
        var numbers = new ArrayList<Integer>();

        //Tamaño
        System.out.println(names.size());

        //Añadir elementos

        names.add("Max");
        names.add("Salas");
        names.add("Castillo");
        System.out.println(names.size());

        //Acceder a los elementos

        System.out.println(names.getFirst());
        System.out.println(names.get(1));
        System.out.println(names.getLast());

        //Modificar los elementos

        names.set(2, "max_salas93@icloud.com");
        System.out.println(names.getLast());

        //Eliminar elementos
        // ya no existe el elemento 2, lo acabamos de eliminar
        names.remove(2);
        System.out.println(names.get(1));

        System.out.println(names.contains("Max"));
        System.out.println(names.contains("max_salas93@icloud.com"));

        //Vaciar ArrayList

        names.clear();
        System.out.println(names.size());

    }
}
