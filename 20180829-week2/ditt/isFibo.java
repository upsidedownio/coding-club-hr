import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    // Complete the solve function below.
    static String solve1(long n) {
        int count=0;
        long fibo = 0;
       while(fibo<=n){
           fibo=fibonacci(count);
           count++;
           if(n==fibo){
               return "IsFibo";
           }
       }
        return "IsNotFibo";

    }
    
    private static long fibonacci(long n){
        if(n<=1){
            return n;
        }else{
           return fibonacci(n-1) + fibonacci(n-2);
        }
    }

    private String solve2(long n){
    	if(allFibos().contains(n)){
    		return "IsFibo";
    	}else{
    		return "IsNotFibo";
    	}
    }

 private static HashSet<Long> allFibos(){
        long a = 1;
        long b = 1;
     
        HashSet<Long> all = new HashSet<>();
        all.add(0L);
        all.add(1L);
        while(b<=10000000000L){
           long  c = a+b;
            all.add(c);
            a=b;
            b=c;
        }
        return all;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            long n = scanner.nextLong();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            String result = solve(n);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}