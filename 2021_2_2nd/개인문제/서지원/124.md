# 문제
<img width="349" alt="124_1" src="https://user-images.githubusercontent.com/78357979/107754304-a1953700-6d64-11eb-9003-dae632b4bc49.PNG">

# 코드
```cpp
#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    string oneTwoFour = "412";

    while (n != 0) {
        answer = oneTwoFour[n % 3] + answer;
        if (n % 3 == 0) { n = n/3 -1; }
        else { n = n / 3; }
    }

    return answer;
}
```
