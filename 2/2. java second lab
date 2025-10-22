import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Создание мультисписка
        List<List<Integer>> multiList = new ArrayList<>();
        
        // Добавление подсписков
        multiList.add(new ArrayList<>(List.of(1, 2, 3)));
        multiList.add(new ArrayList<>(List.of(4, 5, 6)));
        multiList.add(new ArrayList<>(List.of(7, 8, 9)));
        
        System.out.println("Мультисписок:");
        for (List<Integer> row : multiList) {
            System.out.println(row);
        }
        
        // Добавление нового подсписка
        multiList.add(new ArrayList<>(List.of(10, 11, 12)));
        System.out.println("\nПосле добавления:");
        for (List<Integer> row : multiList) {
            System.out.println(row);
        }
        
        // Обращение к элементам
        System.out.println("\nЭлемент [1][2]: " + multiList.get(1).get(2)); // 6
        System.out.println("Элемент [0][0]: " + multiList.get(0).get(0)); // 1
        
        // Изменение элемента
        multiList.get(2).set(1, 88);
        System.out.println("\nПосле изменения [2][1]: " + multiList.get(2));
        
        // Зубчатый мультисписок
        List<List<Integer>> jaggedList = new ArrayList<>();
        jaggedList.add(new ArrayList<>(List.of(1, 2)));
        jaggedList.add(new ArrayList<>(List.of(3, 4, 5, 6)));
        jaggedList.add(new ArrayList<>(List.of(7)));
        jaggedList.add(new ArrayList<>(List.of(8, 9, 10)));
        
        System.out.println("\nЗубчатый мультисписок:");
        for (List<Integer> row : jaggedList) {
            System.out.println(row);
        }
    }
}
