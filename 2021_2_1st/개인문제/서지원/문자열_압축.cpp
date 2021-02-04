#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = 0;
    int string_length = s.length();
    int shortest = string_length;
    for (int i = 1; i <= string_length/2; i++) { //문자 몇개를 기준으로 자를 것인가
        string temp = ""; //압축된 문자열 저장
        int count = 1; //같은 문자 반복횟수 저장
        vector<char>now_words;
        int last_idx = 0;
        while (now_words.size() < i) { now_words.push_back(s[last_idx++]); }
        while (last_idx < string_length) {
            if (string_length - last_idx < i) {
                for (int k = last_idx; k < string_length; k++) {
                    temp += s[k];
                }
                break;
            }
            vector<char>next_words;
            while (next_words.size() < i) { next_words.push_back(s[last_idx++]); }
            if (now_words == next_words) {
                count++;
                continue;
            }
            else {
                if (count > 1) { temp += to_string(count); }
                for (int k = 0; k < now_words.size(); k++) { temp += now_words[k]; }
                now_words = next_words;
                count = 1;
            }
        }
        if (count > 1) { temp += to_string(count); }
        for (int k = 0; k < now_words.size(); k++) { temp += now_words[k]; }
        if (temp.length() < shortest) { shortest = temp.length(); }
        //cout << temp << endl;
    }
    answer = shortest;
    return answer;
}

int main()
{
    cout << solution("aabbaccc") << endl;
}
