package week4;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class TwoTwo {

	/*
	 * Complete the twoTwo function below.
	 */
	static int twoTwo(String a) {
		/*
		 * Write your code here.
		 */
		int result = 0;
		int inputStringSize = a.length();
		// 2의 배수의 위치를 담을 스텍을 준비해준다.
		Stack<Integer> indexStack = new Stack<>(); 

		// 입력 받은 숫자가 2의 배수이며 0이 아님을 체크하고 스텍에 담아준다.
		for (int index = 0; index < inputStringSize; index++) {

			int singleNum = Character.getNumericValue(a.charAt(index));

			if (singleNum % 2 == 0 && singleNum != 0) {
				indexStack.push(index);
			}

		}
		
		// 스텍에 담긴 인덱스 기준으로 앞의 숫자들을 잘라 2의 제곱수임을 확인해준다.
		while(!indexStack.isEmpty()) {
			String checkStr = a.substring(0,indexStack.pop()+1);
			int countPowerOfTwo = countingPowerOfTwo(checkStr);
			result += countPowerOfTwo;
		}

		return result;
	}

	// 숫자를 1의 자리 부터 잘라 2의 제곱수임을 확인해준다.
	// 1의 자리 확인 -> 10의 자리까지 확인
	private static int countingPowerOfTwo(String checkStr) {
		int result = 0;
		for (int index = checkStr.length() - 1; index >= 0; index--) {
			if (checkPowerOfTwo(checkStr.substring(index))) {
				result++;
			}
		}

		return result;
	}

	// 2의 제곱수 인지 확인하여 true를 리턴한다.
	private static boolean checkPowerOfTwo(String check) {

		// 첫 시작이 0이면 false 리턴
		if (checkStartZero(check)) {
			return false;
		}

		int changeInt = Integer.parseInt(check);

		return ((changeInt & (changeInt - 1)) == 0);

		// 수가 커져 int 값을 넘기에 double 로 바꿔 계산 시도
		// 시간이 너무 오래 걸림;;
//		double changeInt = Double.parseDouble(check);
//
//		boolean result = false;
//
//		if (changeInt % 2 != 0) {
//			return false;
//		} else {
//			for (int i = 0; i <= changeInt; i++) {
//				if (Math.pow(2, i) == changeInt) {
//					result = true;
//				}
//			}
//		}

//		return result;

	}

	// 0으로 시작되는 문자열이면 true 리턴
	private static boolean checkStartZero(String check) {

		return check.charAt(0) == '0' ? true : false;
	}

    private static final Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(scanner.nextLine().trim());
//		int t = 1;

		for (int tItr = 0; tItr < t; tItr++) {
            String a = scanner.nextLine();
//			 String a =
//			 "9303535670983768199031344740966458039726609416797671171603074549512182887851493418575245449136173639177760276560207077549242900846267596823817051317718446589520242536874132581700120107002038199303870846751188192899823151552628349788604516295066307994130118526061826166445047808309163001841380667575628151274558987543914186376514799892578820116121531383164833962895501326553806236997089282520174174189206292883439012459432693877366459895758465185873923518437208883287869410049671804351768330228241833181048771841834309240249132277574952747489997467168763400466618303709392785810954982875161446396373040800947562126272731545618170968107390172263733095197200113358841034017182951507037254979515982202834948083154776267844089139019063040156654448338365040715366458968162887836583628774290327941701420576894069006881693378223441337877537377325813845730080900918242835443359855685076558915384842574884883772410178635875682021801984576460752303423488223007451985306231415357182726483615059804162147483648324";
//			String a = "023223";

			int result = twoTwo(a);
//			System.out.println("결과 : " + result);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
		}

        bufferedWriter.close();
	}
}
