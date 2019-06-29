package week6;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Balanced_Brackets {

	// Complete the isBalanced function below.
	static String isBalanced(String input) {
		// 하나씩 담을 스텍
		Stack<Character> bucket = new Stack<Character>();
		// 결과
		String result = NO;
		// stack 에 한번이라도 담았는가 체크
		boolean pushOnce = false;

		for (char one : input.toCharArray()) {
			// 괄호의 시작이면 스텍에 담아준다. 체크 boolean 변경
			if (one == '(' || one == '{' || one == '[') {
				pushOnce = true;
				bucket.push(one);
			} else {
				// stack에 값이 한개라도 차있다면 하기 코드 실행
				if (!bucket.isEmpty()) {
					// 스텍의 마지막 확인
					char lastOne = bucket.peek();
					// 짝이 맞는지 체크
					boolean pair = false;

					switch (one) {
					case ')':
						if (lastOne == '(') {
							pair = true;
						}
						break;
					case '}':
						if (lastOne == '{') {
							pair = true;
						}
						break;
					case ']':
						if (lastOne == '[') {
							pair = true;
						}
						break;
					}
					// 짝이 맞다면 스텍테서 뺴준다.
					if (pair) {
						bucket.pop();
					// 아니면 결과를 NO로 바꿔주고 for 문을 빠져나와 준다.
					}else {
						result = NO;
						break;
					}
				}
			}
		}

		// 모든 글자를 체크한뒤 stack 이 비어있고 stack에 한번이라도 값을 넣었다면 결과를 YES 로 바꿔준다.
		if (bucket.isEmpty() && pushOnce) {
			result = YES;
		}
		return result;
	}

	private static final Scanner scanner = new Scanner(System.in);
	private static final String YES = "YES";
	private static final String NO = "NO";

	public static void main(String[] args) throws IOException {
//		BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

		int t = scanner.nextInt();
		scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

		for (int tItr = 0; tItr < t; tItr++) {
			String s = scanner.nextLine();

			String result = isBalanced(s);
			System.out.println(result);

//			bufferedWriter.write(result);
//			bufferedWriter.newLine();
		}

//		bufferedWriter.close();

		scanner.close();
	}
}
