import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class easy_three{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input the number of rows
        System.out.print("Enter the number of rows for Pascal's Triangle: ");
        int numRows = scanner.nextInt();

        // Call the generate function
        List<List<Integer>> result = generate(numRows);

        // Display the generated Pascal's Triangle
        displayPascalsTriangle(result);

        // Close the scanner
        scanner.close();
    }

    public static List<List<Integer>> generate(int numRows) {
        // Create an array list to store the result
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            row.add(1);
            for (int j = 1; j < i; j++) {
                row.add(res.get(i - 1).get(j - 1) + res.get(i - 1).get(j));
            }
            if (i > 0) {
                row.add(1);
            }
            res.add(row);
        }
        return res;
    }

    public static void displayPascalsTriangle(List<List<Integer>> triangle) {
        System.out.println("Pascal's Triangle:");
        for (List<Integer> row : triangle) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
