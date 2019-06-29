import java.awt.Point;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class CountLuck {

    static int destRow;
    static int destColumn;


    static int count;

    static boolean[][] visited;

    /*
     * Complete the travelAroundTheWorld function below.
     */

    /**
     *
     * empty : .
     * block : X
     * departure : M
     * destination : *
     *
     * (row, column)
     * (0,0) ~ (m-1,n-1)
     * row : top to bottom(ㅣ)
     * column : left to right(ㅡ)
     *
     * direction : left right up down
     */
    // Complete the countLuck function below.
    static boolean countLuck(int row, int column) {
        //visited
        visited[row][column]=true;

        //도착하면 리턴
        if(row ==destRow && column==destColumn)
            return true;

        ArrayList<Point> routes = new ArrayList<Point>();

        //up not visited
        if(row>0&&!visited[row-1][column])
            routes.add(new Point(row-1, column));
        //left not visited
        if(column>0&&!visited[row][column-1])
            routes.add(new Point(row, column-1));

        //down not visited
        if(row<visited.length-1&&!visited[row+1][column])
            routes.add(new Point(row+1, column));

        //right not visited
        if(column<visited[0].length-1&&!visited[row][column+1])
            routes.add(new Point(row, column+1));


        for(Point route : routes) {
            if(countLuck(route.x, route.y)) {
                if(routes.size()>1) {
                    //wand wave (have two ways)
                    count++;
                }
                return true;
            }
        }


        return false;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");


        for(int tItr=0; tItr<t; tItr++) {
            String[] nm = scanner.nextLine().split(" ");

            int n = Integer.parseInt(nm[0]);
            int m = Integer.parseInt(nm[1]);

            int depRow=0;
            int depColumn=0;

            visited = new boolean[n][m];

            for(int i=0; i<n; i++) {
                String matrixItem=scanner.nextLine();
                for(int j=0; j<m; j++) {
                    if(matrixItem.charAt(j)=='X') {
                        //forest
                        visited[i][j] = true;
                    } else if(matrixItem.charAt(j)=='M') {
                        depRow=i;
                        depColumn=j;
                    } else if(matrixItem.charAt(j)=='*') {
                        destRow=i;
                        destColumn=j;
                    }
                }
            }
            int k = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            count = 0 ;
            countLuck(depRow, depColumn);
            System.out.println(k==count?"Impressed":"Oops!");

            scanner.close();
        }

    }

}
