package week4;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class SurfaceArea {

    // Complete the surfaceArea function below.
    static int surfaceArea(int[][] A) {
    	int result = 0;
        
        int column = A.length;
        int row = A[0].length;
        // 입력값이 0보다 크기 때문에 바닥 부분과 천장 부분은 빈 부분이 없다.
        // 2차 배열의 크기에 따른 천장부분과 바닥 부분의 크기를 구해준다.
        int topAndButtomArea = (column * row)*2;
        result += topAndButtomArea;
        
        // 1 행씩 계산 넓이를 구해준다.
        for(int [] i : A){
        	result += calcurateSurface(i);
        }
        
        // 행과 열을 바꿔 준다.
        int [][] reverseA = switchArray(A);
    	// 1 행씩 계산 넓이를 구해준다.
        for(int []i :reverseA) {
        	result += calcurateSurface(i);
        }
                
        return result;

    }
    
    
    // 행열을 바꿔주는 함수
    static int[][] switchArray(int [][]original) {
    	int column = original.length;
    	int row = original[0].length;
    	
    	int [][] reverse = new int[row][column];
    	for(int i = 0; i <original.length; i++) {
    		for(int j = 0 ; j <original[i].length;j++) {
    			reverse[j][i] = original[i][j];
    		}
    	}
    	return reverse;
    }
    
    // 산출해야 하는 넓이를 구해준다.
    // 기본 개념은 하기와 같다.
    // {1,3,2,4} 의 높이를 가진 열의 천장과 바닥을 제외한 3D 넓이를 구하는 방식을 살펴보면
    // 1+2+1+2+4 으로 구할수 있다.
    // 첫 값으로 시작해서 다음 값과의 차이를 모두 더하고 마지막 값을 더해줌으로서 3D 넓이의 산출이 가능하다.
    static int calcurateSurface(int [] oneRow){
        int size = oneRow.length;
        int total = 0;
        total += oneRow[0];
        
        for(int i = 0; i < size-1; i++){
            int current = oneRow[i];
            int next = oneRow[i+1];
            int rise = next > current ? next - current: current - next;
            total += rise;
        }
        
        total += oneRow[size-1];
        
        return total;    
    }


    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] HW = scanner.nextLine().split(" ");

        int H = Integer.parseInt(HW[0]);

        int W = Integer.parseInt(HW[1]);

        int[][] A = new int[H][W];

        for (int i = 0; i < H; i++) {
            String[] ARowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < W; j++) {
                int AItem = Integer.parseInt(ARowItems[j]);
                A[i][j] = AItem;
            }
        }

        int result = surfaceArea(A);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}