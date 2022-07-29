# Author. K9714
# Date. 22.07.29
# Baekjoon. 9012

# Python Version
# 3.8.9

# 조건
# 1. 첫 줄에 1 이상 50 이하의 자연수가 주어짐
# 2. 주어진 자연수만큼 괄호'(',')' 문자열이 주어짐

# 목표
# 1. 완벽한 괄호 문자열이면 YES, 아니면 NO 출력
#---------------------------

# 예시 문제
ex = [
'''6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(''',
'''3
((
))
())(()'''
]

def solution(n, vps_str):
    # 괄호와 같은 수식(전위, 후위 등)은
    # Stack 구조로 해결하는 것이 일반적
    for vps in vps_str:
        vp_stack = []
        check_vps = True
        for vp in vps:
            if vp == '(':
                vp_stack.append(vp)
            elif len(vp_stack) > 0:
                vp_stack.pop(-1)
            else:
                check_vps = False
        if check_vps and len(vp_stack) == 0:    
            print("YES")
        else:
            print("NO")

for e in ex:
    inputs = e.split('\n')
    n = int(inputs[0])
    vps_str = inputs[1:]
    solution(n, vps_str)
