import java.util.Scanner;
import java.util.*;
public class Main {
    static int MX[]={1,-1,0,0};
    static int MY[]={0,0,-1,1};
    static boolean visit[][]=new boolean[100][100];
    static int count;
    static int first_n,first_m,last_n,last_m,n,m;

    public static boolean chk(char f[][],int a,int b){//갈수있는 방향이 2개 이상인지 체크하는 함수
        int tmp=0;
        for(int i=0;i<4;i++){
            if(visit[a+MX[i]][b+MY[i]]==false&&a+MX[i]<n&&b+MY[i]<m&&f[a+MX[i]][b+MY[i]]!='X')
                tmp++;
        }
        if(tmp>1)
            return true;

        return false;
    }

    public static boolean dfs(char f[][],int a,int b,int cnt){
        visit[a][b]=true;
        if(chk(f,a,b))
            cnt--;

        if(a==last_n&&b==last_m){
            if(cnt==0)
                return true;
            else
                return false;
        }
        for(int i=0;i<4;i++){
            if(visit[a+MX[i]][b+MY[i]]==false&&a+MX[i]<n&&b+MY[i]<m&&f[a+MX[i]][b+MY[i]]!='X')
                dfs(f,a+MX[i],b+MY[i],cnt);
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testcase = sc.nextInt();
        for (int i = 0; i < testcase; i++) {
            m=sc.nextInt();
            n=sc.nextInt();

            char forest[][]=new char[n][m];
            for(int p=0;p<n;p++){
                for(int k=0;k<m;k++){
                    forest[p][k]=sc.next().charAt(0);
                    visit[p][k]=false;
                    if(forest[p][k]=='M'){
                        first_n=p;
                        first_m=k;
                    }
                    else if(forest[p][k]=='*'){
                        last_n=p;
                        last_m=k;
                    }
                }
            }
            count=sc.nextInt();

            if(dfs(forest,n,m,count)){
                System.out.print("Impressed");
            }
            else
                System.out.print("Oops!");
        }


    }
}
