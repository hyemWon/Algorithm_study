# 2007년 (백준: 1924번)
# 오늘이 2007년 1월 1일 월요일 -> 2007년 x월 y일 요일 맞추기
# 1,3,5,7,8,10,12월은 31일까지
# 4,6,9,11월은 30일까지
# 2월은 28일까지

from sys import stdin

# 1) 구하려는 날짜와 기준일 사이의 날 수 계산
# 2) 날 수를 요일로


def cal_week(month, day):
    days = 0
    cnt_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    #날 수 계산
    for i in range(month-1):
        days += cnt_days[i]
    days += day
    # 요일로 매칭
    print(week[days%7])


if __name__=="__main__":
    x, y = map(int, stdin.readline().split())
    cal_week(x, y)
