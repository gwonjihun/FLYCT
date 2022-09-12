# 백준[1461] 도서관
'''
문제
현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 
각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 

입력
첫째 줄에 책의 개수 N과, 세준이가 한 번에 들 수 있는 책의 개수 M이 주어진다. 
둘째 줄에는 책의 위치가 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 
책의 위치는 0이 아니며, 절댓값은 10,000보다 작거나 같은 정수이다.

예제 입력 1
7 2
-37 2 -6 -39 -29 11 -28

예제 출력 1
131

예제 입력 2
8 3
-18 -9 -4 50 22 -26 40 -45

예제 출력 2
158

예제 입력 3
6 2
3 4 5 6 11 -1

예제 출력 3
29

예제 입력 4
1 50
1

예제 출력 4
1
'''

import sys
input = sys.stdin.readline

# 책의 개수 N과 한 번에 들 수 있는 책의 개수 M
N, M = map(int, input().split())
# 책의 위치
books = sorted(list(map(int, input().split())))
# 음수, 양수 나누기
minus = list(filter(lambda x: x<0, books))
plus = list(filter(lambda x: x>0, books))
# 움직이는 거리
move = 0

# 음수 부분 이동 거리
while minus:
    # 이동 후 다시 원점으로 돌아가 책을 들어야 하기 때문에 2 곱해줌
    move += abs(minus[0])*2
    # 남은 책이 M개보다 작은 경우 멈춤
    if len(minus) <= M:
        break
    # 왼쪽에서 오른쪽으로 M개씩 이동
    minus = minus[M:]
    
# 양수 부분 이동 거리
while plus:
    # 이동 후 다시 원점으로 돌아가 책을 들어야 하기 때문에 2 곱해줌
    move += plus[-1]*2
    # 남은 책이 M개보다 작은 경우 멈춤
    if len(plus) <= M-1:
        break
    # 오른쪽에서 왼쪽으로 M개씩 이동
    plus = plus[:-M]

# 절댓값 중 가장 큰 수 빼주기(마지막 이동시에 0으로 돌아가지 않아도 되기 때문)
move -= max(abs(books[0]), abs(books[-1]))

print(move)