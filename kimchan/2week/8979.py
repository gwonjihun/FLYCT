'''
1. 금메달 수가 더 많은 나라
2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

등수가 같으면 둘 다 같은 등수로 표기, 단 비어있는 횟수만큼 뒷 나라의 랭킹은 밀린다.
'''

# Solution1
import sys
input = sys.stdin.readline

result = {}
N, K = map(int, input().split())

dict = {}
arr = []
for _ in range(N):
    buf = list(map(int, input().split()))
    dict[buf.pop(0)] = buf
    arr.append(buf)

for _ in reversed(range(3)):
    arr = sorted(arr, key=lambda x:-x[_])
rank = {}
for idx, i in enumerate(arr):
    for k, v in dict.items():
        if i == v:
            if v not in rank.values():
                rank[idx+1] = v
for k, v in rank.items():
    if dict[K] == v:
        print(k)

# Solution2
import sys
input = sys.stdin.readline
input_datas = list(map(int, input().split(" ")))
datas = []
for i in range(input_datas[0]):
    datas.append(list(map(int, input().split(" "))))

checker = 1e9 # 나올 수 없는 최대값 초기 선언
result = {} # 해당 국가가 몇 등인지 출력하기 위한 딕셔너리 생성
for i in reversed(range(1, 4)):
    datas = sorted(datas, key=lambda x: -x[i])

idx_buf = 0
for idx, buf in enumerate(datas):
    if checker != buf[1:]:
        checker = buf[1:]
        result[buf[0]] = idx+1
        idx_buf = idx+1
    else:
        result[buf[0]] = idx_buf

print(result[input_datas[1]])
