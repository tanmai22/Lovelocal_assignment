import java.util.Scanner;

public class easy_one {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input a string
        System.out.print("Enter a string: ");
        String inputString = scanner.nextLine();

        // Call the lengthOfLastWord function
        int res = lengthOfLastWord(inputString);

        // Display the result
        System.out.println("Length of the last word: " + res);

        // Close the scanner
        scanner.close();
    }

    public static int lengthOfLastWord(String s) {
        if (s.length() == 0) {
            return 0;
        }

        String str = s.trim();
        int cnt = 0;
        int i = str.length() - 1;

        while (i >= 0 && str.charAt(i) != ' ') {
            i--;
            cnt++;
        }

        return cnt;
    }
}
