#include <vector>
#include <iostream>

using namespace std;
int dfs(vector<vector<int>>&picture, vector<vector<int>>&check, int num, int row, int column) {
    if (row < 0 || column < 0) { return 0; }
    else if (row >= picture.size() || column >= picture[0].size()) { return 0; }
    else if (picture[row][column] != num || check[row][column] != 0) { return 0; }
    else {
        int size = 0;
        check[row][column]++;
        size++;
        size += dfs(picture, check, num, row - 1, column);
        size += dfs(picture, check, num, row, column - 1);
        size += dfs(picture, check, num, row + 1, column);
        size += dfs(picture, check, num, row, column + 1);
        return size;
    }
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    vector<vector<int>>check(m, vector<int>(n, 0));

    for (int row = 0; row < m; row++) {
        for (int column = 0; column < n; column++) {
            if (picture[row][column] == 0) { continue; }
            else if (check[row][column] != 0) { continue; }
            else {
                number_of_area++;
                int temp_area_size = dfs(picture, check, picture[row][column], row, column);
                if (max_size_of_one_area < temp_area_size) { max_size_of_one_area = temp_area_size; }
            }
        }
    }

    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
