# Author. K9714
# Date. 22.07.29
# Baekjoon. 1541

# Python Version
# 3.8.9

# 조건
# 1. 더하기, 빼기, 숫자만 존재
# 2. 0으로 시작하는 숫자 존재
# 3. 수식의 길이는 <= 50
# 4. 연속되는 숫자는 최대 5번까지
# 5. 처음과 마지막은 무조건 숫자

# 목표
# 괄호를 최소로 사용하여 최솟값 만들기
#----------------------------------------

# 예시 문제
ex = [
    "55-50+40",     # -35
    "10+20+30+40",  # 100
    "00009-00009"   # 0
    "34-00009+34+43-00002+234-1234+123-4"
]

import re

def solution(expression):
    # 먼저 수식과 숫자를 분리
    # 정규표현식을 이용한 분리(수식은 + 및 - 만 존재)
    numbers = re.split(r"[\+\-]", expression)
    opers = re.split(r"[0-9]+", expression)[1:-1]
    
    # 0 제거를 위한 필터링
    numbers = list(map(lambda x: int(x), numbers))

    # 뺄셈 뒤의 항을 최대로 만들기
    # 뺄셈 항 index 찾기
    exp_sub_idxs = list(filter(lambda x: opers[x] == '-', range(len(opers))))
    
    # 다음 뺄셈 항까지 괄호 치기
    exec_exp = "" # 변화시킬 수식 문자열
    brk = False # 괄호 open 여부
    for i, n in enumerate(numbers):
        # 먼저 수식에 숫자를 추가
        exec_exp += f"{n}"
        # 뺄셈항인 경우 뺄셈 이후 괄호 추가
        if i in exp_sub_idxs:
            # 괄호 open 상태인 경우 close
            if brk:
                exec_exp += ")"
            brk = True
            exec_exp += "-("
        elif i < len(numbers) - 1:
            exec_exp += "+"

    # open 상태인 괄호 닫기
    if brk:
        exec_exp += ")"
    print(exec_exp)
    # 수식 만들어서 계산시키기
    exec(f"print({exec_exp})")

for e in ex:
    solution(e)
