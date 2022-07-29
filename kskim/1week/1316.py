# Author. K9714
# Date. 22.07.29
# Baekjoon. 1316

# Python Version
# 3.8.9

# 조건
# 1. 첫 줄에 1 이상 100 이하의 자연수가 주어짐
# 2. 이후 주어진 자연수만큼의 단어가 주어짐
# 3. 단어는 모두 알파벳 소문자로 이루어짐
# 4. 알파벳 단위 별 붙어서 나타나는 단어는 그룹 단어

# 목표
# 1. 그룹 단어 개수 출력
#---------------------------

# 예시 문제
ex = [
'''3
happy
new
year''',
'''4
aba
abab
abcabc
a''',
'''5
ab
aa
aca
ba
bb''',
'''2
yzyzy
zyzyz''',
'''1
z'''
]

def solution(n, words):
    # 그룹 단어 체크를 위한 변수
    cnt = 0
    # 단어 배열 전개
    for word in words:
        # 확인한 알파벳 배열 검사
        check_alpha = []
        # 현재 확인중인 알파벳
        target = None
        # 그룹 단어 체크용 변수
        check_cnt = True
        # 단어 알파벳 전개
        for w in word:
            # 본 적 없는 알파벳이면 append
            # 확인중 알파벳을 해당 단어로 변경
            if w not in check_alpha:
                check_alpha.append(w)
                target = w
            # 만약 본적이 있으면서, 확인중인 단어가 아니면 루프 종료
            elif target != w:
                check_cnt = False
                break
        # 검사 오류가 없으면 카운트
        if check_cnt:
            cnt += 1
    # 결과 출력
    print(cnt)

for e in ex:
    inputs = e.split('\n')
    n = int(inputs[0])
    words = inputs[1:]
    solution(n, words)
