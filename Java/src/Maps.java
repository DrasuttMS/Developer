import java.util.HashMap;

public class Maps {
    public static void main(String[] args) {

        //Declaracion y Creaacion
        HashMap<String, String> names = new HashMap<>();
        var numbers = new HashMap<Integer, String>();

        //Tamaño
        System.out.println(names.size());

        //Añadir elementos
        names.put("Max", "mba.salas@gmail.com");
        names.put("Salas", "mba@gmail.com");
        names.put("Drasutt", "max_salas@icloud.com");
        System.out.println(names.size());
        System.out.println(names);

        //Acceder a los elementos

        System.out.println(names.get("Drasutt"));
        System.out.println(names.get("Dev"));

        //Verificar elementos

        System.out.println(names.containsKey("Drasutt"));
        System.out.println(names.containsKey("Dev"));

        System.out.println(names.containsValue("Drasutt"));
        System.out.println(names.containsValue("Dev"));

        //Eliminar elemnetos

        System.out.println(names.remove("Max"));
        System.out.println(names.remove("Drasutt"));
        System.out.println(names);

        //Limpiar HashMap
        names.clear();
        System.out.println(names);

        //Otras operaciones

    }
}
