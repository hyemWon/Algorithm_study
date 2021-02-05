#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    vector<vector<int>> triangle;
    for (int i = 1; i <= n; i++) { triangle.push_back(vector<int>(i)); }

    int row = 0, column = 0, num = 1;
    for(int temp=0; temp<=n/3+1; temp++) {
        //종료조건 (row, column이 범위를 벗어남, 이미 숫자가 저장됨)
        int stat = 0;
        //1. 세로방향 이동
        for (; row < n && triangle[row][column] == 0; row++) {
            triangle[row][column] = num++;
        }

        row--;

        //2. 가로방향 이동
        for (column += 1; column < triangle[row].size() && triangle[row][column] == 0; column++) {
            triangle[row][column] = num++;
        }

        column--;
        
        //3. 대각선 윗방향 이동
        for (row -= 1, column -= 1; triangle[row][column] == 0; row--, column--) {
            triangle[row][column] = num++;
        }

        row+=2, column++;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            answer.push_back(triangle[i][j]);
        }
    }

    return answer;
}
