int surfaceArea(vector<vector<int>> A) {

    int INT_Result;
    int INT_BuffBlockNum;

    INT_Result = 0;

    for (int i0 = 0; i0 < A.size(); i0++) {
        for (int i1 = 0; i1 < A[i0].size(); i1++) {
            //가로, 세로 블럭 갯수 차이 = 표먼적

            //가로
            if (i0 == 0) {
                INT_BuffBlockNum = 0;//모서리
            } else {
                INT_BuffBlockNum = A[i0 - 1][i1];
            }

            INT_Result = INT_Result + abs(A[i0][i1] - INT_BuffBlockNum);

            //세로
            if (i1 == 0) {
                INT_BuffBlockNum = 0;//모서리
            } else {
                INT_BuffBlockNum = A[i0][i1 - 1];
            }

            INT_Result = INT_Result + abs(A[i0][i1] - INT_BuffBlockNum);

            //모서리
            if (i0 == A.size() - 1) {
                INT_Result = INT_Result + A[i0][i1];
            }
            if (i1 == A[i0].size() - 1) {
                INT_Result = INT_Result + A[i0][i1];
            }
        }

    }

    //윗면 or 아랫면 갯수

    INT_BuffBlockNum = 0;
    for (int i0 = 0; i0 < A.size(); i0++) {
        for (int i1 = 0; i1 < A[i0].size(); i1++) {
            INT_BuffBlockNum++;
        }
    }
    //총합
    INT_Result = INT_Result + INT_BuffBlockNum + INT_BuffBlockNum;

    return INT_Result;
}