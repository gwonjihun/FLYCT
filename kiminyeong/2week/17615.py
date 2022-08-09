# [백준 17615] 볼 모으기
'''
문제
빨간색 볼과 파란색 볼이 <그림 1>에서 보인 것처럼 일직선상에 섞여 놓여 있을 때, 
볼을 옮겨서 같은 색 볼끼리 인접하게 놓이도록 하려고 한다. 볼을 옮기는 규칙은 다음과 같다.

1. 바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길 수 있다. 
    즉, 빨간색 볼은 옆에 있는 파란색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다. 
    유사하게, 파란색 볼은 옆에 있는 빨간색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다.
2. 옮길 수 있는 볼의 색깔은 한 가지이다. 
    즉, 빨간색 볼을 처음에 옮겼으면 다음에도 빨간색 볼만 옮길 수 있다. 유사하게, 파란색 볼을 처음에 옮겼으면 다음에도 파란색 볼만 옮길 수 있다.

입력
첫 번째 줄에는 볼의 총 개수 N이 주어진다. (1 ≤ N ≤ 500,000) 
다음 줄에는 볼의 색깔을 나타내는 문자 R(빨간색 볼) 또는 B(파란색 볼)가 공백 없이 주어진다. 
문자열에는 R 또는 B 중 한 종류만 주어질 수도 있으며, 이 경우 답은 0이 된다.

출력
최소 이동횟수를 출력한다.

예제 입력 1
9
RBBBRBRRR

예제 출력 1
2

예제 입력 2
8
BBRBBBBR

예제 출력 2
1
'''

import sys
input = sys.stdin.readline

# 볼의 총 개수 N
N = int(input().rstrip())
# 볼의 색깔을 나타내는 문자 R 또는 B가 공백 없이 주어짐
colors = input().rstrip()
# 파랑, 빨강 공 각각의 개수 (둘 중 더 적은 개수의 볼 옮기기)
blue = colors.count('B')
red = colors.count('R')
# 왼쪽으로 옮기기
left_color = colors[0]
left = colors.lstrip(left_color).count(left_color)
# 오른쪽으로 옮기기
right_color = colors[-1]
right = colors.rstrip(right_color).count(right_color)
# 최소 이동 수 출력
print(min(blue, red, left, right))