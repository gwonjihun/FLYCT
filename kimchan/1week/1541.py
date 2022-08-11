'''
잃어버린 괄호
문제의 핵심은 여러 계산식의 경우의 수 중에, 가장 적은 수의 값을 찾는 것
그러려면, 식 내의 +연산을 먼저 진행하고, 마지막에 전부 - 해주어야 가장 작은값을 얻을 수 있다.
'''

# 아래 두 줄은 입력을 받아올 때 더 빠르게 받아오기 위함(차이 큼)
import sys
input = sys.stdin.readline

# 데이터를 임시 저장할 리스트 선언
arr = []

# 중복되지 않을 임의의 숫자(초기값) 설정
result = 12301230

# 식 받아오기
func = input().strip()

# 먼저, -연산자를 기준으로 문자들을 나눠 리스트에 저장한다.
arr = func.split("-")

# 인덱스와 리스트의 값을 순차적으로 꺼내온다.
for idx, num in enumerate(arr):
    # 만약 -연산자를 기준으로 나눴다면, +연산자의 모든 값을 더한다.
    if "+" in num:
        buf = map(int, num.split("+"))
        arr[idx] = sum(buf)
    else:
        arr[idx] = int(num)

# 각 +연산을 진행한 값을 순차적으로 뺀다.
for i in arr:
    # 만약 첫번째 값이라면, 그냥 값을 넣고
    if result == 12301230:
        result = i
    # 두번째 값 부터 빼준다.
    else:
        result -= i

# 출력한다.
print(result)
