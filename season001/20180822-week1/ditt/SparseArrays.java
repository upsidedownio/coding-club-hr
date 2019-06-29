import java.io.*;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.Scanner;
import java.util.concurrent.*;
import java.util.regex.*;

public class SparseArrays {

    //    Complete the matchingStrings function below.
    static int[] matchingStrings(String[] strings, String[] queries) {

        int[] arr = new int[queries.length];

        for(int i=0;i<strings.length;i++){
            for (int j = 0 ; j < queries.length; j++){
                if(strings[i].equals(queries[j])){
                    arr[j]+=1;
                }
            }
        }

        return arr;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(new File("output.txt")));

        int stringsCount = scanner.nextInt();

        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String[] strings = new String[stringsCount];

        for (int i = 0; i < stringsCount; i++) {
            String stringsItem = scanner.nextLine();
            strings[i] = stringsItem;
        }

        int queriesCount = scanner.nextInt();
        System.out.println("question count "+queriesCount);

        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String[] queries = new String[queriesCount];

        for (int i = 0; i < queriesCount; i++) {
            String queriesItem = scanner.nextLine();
            queries[i] = queriesItem;
        }

        int[] res = matchingStrings(strings, queries);

        for (int i = 0; i < res.length; i++) {
            bufferedWriter.write(String.valueOf(res[i]));
            System.out.println(String.valueOf(res[i]));

            if (i != res.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
