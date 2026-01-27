public class Strings {
    public static void main(String[] args) {
        var name = "maximiliano";
        //Comparacion
        System.out.println(name.equalsIgnoreCase("Maximiliano"));

        // == vs. equals

        var a = "max";
        var b = "max";
        var c = new String("max");

        System.out.println(a == b);
        System.out.println(a == c);
        System.out.println(a.equals(c));

        //Operaciones de reemplazo o de limpieza Trim

        //trim elimina espacio vacios sobrantes
        System.out.println(" Hola , mi nombre es Max Salas  ".trim());

        //replace
        System.out.println(" Hola , mi nombre es Max Salas  ".replace("Max","Maximiliano"));

        //format
        var mm = "Max Salas";
        var nn = 32;
        String.format("Hola, Max Salas es mi nombre");

        //Para modificar dentro de una cadena y usar una variable de distintos formatos puedo reemplazar por;
        // %s -> para texto, %d -> para numeros enteros, %f -> para numeros flotantes
        System.out.println(String.format("Hola, %s es mi edad es %d",mm, nn));
    }
}
