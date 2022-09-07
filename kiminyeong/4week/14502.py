# [백준 14502] 연구소
'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

- 0: 빈칸
- 1: 벽
- 2: 바이러스
'''
import copy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 연구소
labs = []
# 빈 칸
empty = []
# 바이러스
virus = []
# 최대 안전 영역
max_safe = 0

# 빈 칸 인덱스 찾기
for y in range(n):
    # 연구소
    labs.append(list(map(int, input().split())))
    for x, l in enumerate(labs[y]):
        # 빈 칸인 경우에 벽을 세울 수 있기 때문에 0(빈 칸)인 인덱스만 배열에 추가
        if l == 0:
            empty.append((y, x))
        elif l == 2: # 바이러스 인덱스
            virus.append((y, x))

# 바이러스 퍼트리기 함수
def dfs(labs):
    # 방문한 칸 기록
    visited = [[False]*m for _ in range(n)]
    q = deque()
    # 바이러스 담기
    for (y, x) in virus:
        q.append((y, x))

    while q:
        # 현재 위치
        cy, cx = q.popleft()
        # 사방면 확인
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            # 다음 칸이 방문하지 않은 빈 칸이면 바이러스 퍼짐
            if (0 <= nx < m) and (0 <= ny < n) and (labs[ny][nx] == 0) and (visited[ny][nx] == False):
                labs[ny][nx] = 2
                visited[ny][nx] = True
                q.append((ny, nx))

# 빈 칸 세 군데 벽으로 막기
for wall in combinations(empty, 3):
    # 원본 훼손을 막기 위해 연구소 초기값 복사하여 사용
    temp_labs = copy.deepcopy(labs)

    # 벽 세우기
    for (y, x) in wall:
        temp_labs[y][x] = 1
    
    # 바이러스 퍼트리기
    dfs(temp_labs)

    # 안전 영역 탐색하기
    safe = 0
    for raw in temp_labs:
        safe += raw.count(0)

    # 현재 안전 영역이 최대 안전 영역이면 갱신
    if safe > max_safe:
        max_safe = safe
    
print(max_safe)