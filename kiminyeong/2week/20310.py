# [백준 20310] 타노스
'''
문제
어느 날, 타노스는 0과 1로 이루어진 문자열 S를 보았다. 
신기하게도, S가 포함하는 0의 개수와 S가 포함하는 1의 개수는 모두 짝수라고 한다.

갑자기 심술이 난 타노스는 S를 구성하는 문자 중 절반의 0과 절반의 1을 제거하여 새로운 문자열 S'를 만들고자 한다. 
S'로 가능한 문자열 중 사전순으로 가장 빠른 것을 구하시오.

입력
문자열 S가 주어진다.

출력
S'로 가능한 문자열 중 사전순으로 가장 빠른 것을 출력한다.

서브 태스크
S의 홀수 번째 문자는 1, 짝수 번째 문자는 0이다.
'''

import sys
# 문자열 S
S = sys.stdin.readline().rstrip()

# 1, 0 개수 카운트
one, zero = 0, 0
for num in S:
    if num == '0':
        zero += 1
    else:
        one += 1

# 절반 만들기
one, zero = one//2, zero//2
while one: # 왼쪽에서부터 1 없애기
    one_idx = S.find('1')
    S = S[:one_idx]+S[one_idx+1:]
    one -= 1
while zero: # 오른쪽에서부터 0 없애기
    zero_idx = S.rfind('0')
    S = S[:zero_idx] + S[zero_idx+1:]
    zero -= 1

print(S)
