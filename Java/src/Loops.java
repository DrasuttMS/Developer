import javax.swing.plaf.synth.SynthTextAreaUI;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Loops {
    public static void main(String[] args) {

        //Loops

        //Bucle For, se ejecuta hasta que se cumpla la condicion

        for (int index = 1; index <= 5; index+=2) {
            System.out.println("Hola, Max");
        }

        //Recorriendo un Array con el ciclo for
        String[] names = {"Max", "Salas", "Castillo"};

        for (int index = 0;index < names.length; index++) {
            System.out.println(names[index]);
        }

        //For-each -> para cada elemento recorre

        for (String name: names){
            System.out.println(name);
        }

        HashSet<Integer> numbers = new HashSet<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(4);
        numbers.add(5);

        for (Integer number:numbers){
            System.out.println(number);
        }

        //Ciclo for each dentro de un mapa
        HashMap<String, String> emails = new HashMap<>();
        emails.put("Max","mba.salas@gmail.com");
        emails.put("Mono","max_salas93@icloud.com");
        emails.put("Drasutt","developer.mba.sc@gmail.com");

        for (Map.Entry<String,String> email: emails.entrySet()){
            System.out.println(email.getKey());;
            System.out.println(email.getValue());;
        }
        //Bucle While

        int index = 0;
        while (index < 5){
            System.out.println(index);
            index++;
        }
        index = 0;
        boolean find = false;
        while (!find){
            System.out.println(names[index]);
            if (names[index].equals("Max")){
                find = true;
            }
            index++;
        }

        // do-while, minimo se ejecuta 1 vez, ejecuta y despues valida la condicion
        index = 0;
        do {
            System.out.println("Hola, Java!!");
            index++;
        }while (index < 0);

        //Control de Bucles

        //break termina el bucle

        for (String name: names){
            if (name.equals("Max")){
                break;
            }
            System.out.println(name);
        }

        //continue

        for (int i = 0; i < 5; i++){
            if (i  == 3){
                continue;
            }
            System.out.println(i);
        }
    }
}
