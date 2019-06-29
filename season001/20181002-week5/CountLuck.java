package week5;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

class Address {
	int x, y;

	Address(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public Address() {
	}
}

class Cell {
	Address addressInfo;
	boolean ableToMove;
	boolean[] pathInfo = { false, false, false, false };
	int waveCount = 0;
	boolean startPoint = false;
	boolean endPoint = false;
	boolean crossPath = false;

	public Cell(Address addressInfo) {
		this.addressInfo = addressInfo;
	}

	public Cell() {
	}

}

public class CountLuck {

	private static final Scanner scanner = new Scanner(System.in);
	private static Address startCell;
	static Stack<Address> moveHistory;
	static Stack<Integer> waveCountStack;
	static int resultWave;

	public static void main(String[] args) throws IOException {
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

		int t = scanner.nextInt();
		scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

		for (int i = 0; i < t; i++) {
			moveHistory = new Stack<Address>();
			waveCountStack = new Stack<Integer>();
			String[] nm = scanner.nextLine().split(" ");

			int row = Integer.parseInt(nm[0]);

			int column = Integer.parseInt(nm[1]);

			Cell[][] detailMap = new Cell[row][column];

			detailMap = settingInputMap(row, column);
			detailMap = settingPathInfo(detailMap);

			int k = scanner.nextInt();
			scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
			moveShell(detailMap, startCell, 0);
			String result = "";
			if (resultWave == k) {
				result = "Impressed";
			} else {
				result = "Oops!";
			}
			System.out.println(result);
//            bufferedWriter.write(result);
//            bufferedWriter.newLine();
		}

//        bufferedWriter.close();

		scanner.close();
	}

	// CellAddress 의 위치로 현재 위치를 이동시킵니다.
	// 입력값 중 waveCount 이동전 위치의 cell에 저장되어 있는 waveCount
	private static void moveShell(Cell[][] detailMap, Address cellAddress, int waveCount) {

		// 이동전 위치의 waveCount 값을 현재 위치한 위치의 waveCount 로 대체해 줍니다.
		detailMap[cellAddress.x][cellAddress.y].waveCount = waveCount;

		// 현재 위치가 스타팅 포인트인지 확인해줍니다.
		if (detailMap[cellAddress.x][cellAddress.y].startPoint == true) {
			// 스타팅 위치이면서 갈림길이면 crossPath를 true로 변경
			if (checkCrossPath(detailMap[cellAddress.x][cellAddress.y].pathInfo) > 1) {
				detailMap[cellAddress.x][cellAddress.y].crossPath = true;
			}
		}

		// 현재 위치가 갈림길이면 waveCount 를 1 증가시켜 주고 moveHistory에 Address를 추가해줍니다.
		if (detailMap[cellAddress.x][cellAddress.y].crossPath) {
			// 첫 갈림길이면 waveCount 를 1로 초기화 해줍니다.
			// 도착지가 아닌 막다른길일때, 첫 갈림길로 출발지를 다시 세팅해줄때 사용 됩니다.
			if (moveHistory.isEmpty()) {
				detailMap[cellAddress.x][cellAddress.y].waveCount = 1;
			} else {
				detailMap[cellAddress.x][cellAddress.y].waveCount++;
			}
			moveHistory.push(cellAddress);
		}

		// 현재 위치가 도착지임을 확인해 줍니다.
		if (detailMap[cellAddress.x][cellAddress.y].endPoint == true) {

			// 현재 위치까지 도달할떄 까지의 waveCount 를 waveCountStack에 저장해줍니다.
			waveCountStack.push(detailMap[cellAddress.x][cellAddress.y].waveCount);
			// moveHistory에 저장되어있는 갈림길 정보가 있는지 확인
			if (!moveHistory.isEmpty()) {
				// 도착지 바로전에 지나온 갈림길로 다시 이동
				Address beforeCross = moveHistory.pop();
				moveShell(detailMap, beforeCross, detailMap[beforeCross.x][beforeCross.y].waveCount);
			}

			// 도착지이고 더이상의 갈림길 정보가 없다면 waveCount중 최소값을 구해줍니다.
			resultWave = countingResult(waveCountStack);

		}

		// 현재 위치의 연결길 상황을 불러옵니다.
		boolean[] pathInfo = detailMap[cellAddress.x][cellAddress.y].pathInfo;
		char nextDirection = 0;
		// 어느 방향으로 연결이 되어있는지 체크
		for (int i = 0; i < pathInfo.length; i++) {

			if (pathInfo[i] == true) {

				switch (i) {
				case 0:
					nextDirection = 'w';
					break;
				case 1:
					nextDirection = 'n';
					break;
				case 2:
					nextDirection = 's';
					break;
				case 3:
					nextDirection = 'e';
					break;
				}
				// 앞으로 이동할 연결방향의 값을 false 로변경
				detailMap[cellAddress.x][cellAddress.y].pathInfo[i] = false;

				// 앞으로 이동할 연결 방향을 제외하고 갈림길인지 다시체크
				detailMap[cellAddress.x][cellAddress.y].crossPath = checkCrossPath(
						detailMap[cellAddress.x][cellAddress.y].pathInfo) > 2 ? true : false;
				break;
			}
		}

		// 막다른 길일때
		if (nextDirection == 0) {
			// 막다른 길이자 도착지는 아니지만 아직 안가본 갈림길이 있을떄
			if (!moveHistory.isEmpty()) {
				Address beforeCross = moveHistory.pop();
				moveShell(detailMap, beforeCross, detailMap[cellAddress.x][cellAddress.y].waveCount);
			} else {
				return;
			}
		}

		Cell nextCell = new Cell();
		Address nextCellAddress = new Address();

		// 다음 위치로 넘어가기전에 다음 위치의 들어오는 길의 정보를 false로 변경
		switch (nextDirection) {
		case 'w':
			nextCellAddress = new Address(cellAddress.x, cellAddress.y - 1);
			nextCell = detailMap[cellAddress.x][cellAddress.y - 1];
			nextCell.pathInfo[3] = false;
			break;
		case 'n':
			nextCellAddress = new Address(cellAddress.x - 1, cellAddress.y);
			nextCell = detailMap[cellAddress.x - 1][cellAddress.y];
			nextCell.pathInfo[2] = false;
			break;
		case 's':
			nextCellAddress = new Address(cellAddress.x + 1, cellAddress.y);
			nextCell = detailMap[cellAddress.x + 1][cellAddress.y];
			nextCell.pathInfo[1] = false;
			break;
		case 'e':
			nextCellAddress = new Address(cellAddress.x, cellAddress.y + 1);
			nextCell = detailMap[cellAddress.x][cellAddress.y + 1];
			nextCell.pathInfo[0] = false;
			break;
		}
		moveShell(detailMap, nextCellAddress, detailMap[cellAddress.x][cellAddress.y].waveCount);

	}

	// 도착지에 도달하기 까지의 waveCount를 모아 최저 값을 확인한다.
	private static int countingResult(Stack<Integer> waveCountStack2) {
		int smallWave = waveCountStack2.pop();
		while (!waveCountStack2.empty()) {
			int newNum = waveCountStack2.pop();
			smallWave = smallWave < newNum ? smallWave : newNum;

		}
		return smallWave;
	}

	//각 위치별로 연결 정보를 세팅해준다.
	private static Cell[][] settingPathInfo(Cell[][] detailMap) {
		Cell[][] map = detailMap;

		for (int i = 0; i < detailMap.length; i++) {
			for (int j = 0; j < detailMap[0].length; j++) {
				if (detailMap[i][j].ableToMove) {
					boolean n = false, s = false, e = false, w = false;

					if (i != 0) {
						boolean moveAble = map[i - 1][j].ableToMove;
						if (moveAble) {
							n = true;
						}
					}

					if (i != detailMap.length - 1) {
						boolean moveAble = map[i + 1][j].ableToMove;
						if (moveAble) {
							s = true;
						}
					}

					if (j != 0) {
						boolean moveAble = map[i][j - 1].ableToMove;
						if (moveAble) {
							w = true;
						}
					}

					if (j != detailMap[0].length - 1) {
						boolean moveAble = map[i][j + 1].ableToMove;

						if (moveAble) {
							e = true;
						}
					}

					boolean[] pathInfo = { w, n, s, e };

					// 갈림길인지 체크
					map[i][j].crossPath = checkCrossPath(pathInfo) > 2 ? true : false;
					map[i][j].pathInfo = pathInfo;

				}
			}
		}

		return map;
	}

	// 갈림길 체크
	private static int checkCrossPath(boolean[] pathInfo) {
		int connectPathNum = 0;

		for (boolean singlePath : pathInfo) {

			if (singlePath == true) {

				connectPathNum++;
			}
		}

		return connectPathNum;
	}
	
	
	// 지도 정보를 입력받아 cell의 배열로 변환해준다.
	private static Cell[][] settingInputMap(int row, int column) {
		Cell[][] map = new Cell[row][column];

		for (int i = 0; i < row; i++) {

			String line = scanner.nextLine();
			for (int j = 0; j < column; j++) {

				Address address = new Address(i, j);
				Cell singleCell = new Cell(address);
				switch (line.charAt(j)) {
				case 'X':
					singleCell.ableToMove = false;
					break;
				case 'M':
					singleCell.ableToMove = true;
					singleCell.startPoint = true;
					startCell = address;
					break;
				case '*':
					singleCell.ableToMove = true;
					singleCell.endPoint = true;

					break;
				case '.':
					singleCell.ableToMove = true;
					break;
				}
				map[i][j] = singleCell;
			}

		}
		return map;
	}

}
