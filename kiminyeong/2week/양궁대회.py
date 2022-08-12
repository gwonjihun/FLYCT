# [프로그래머스] 양궁대회
'''
1, 2는 통과, 3, 4는 시간초과..
'''
from itertools import product

def solution(n, info):
    a_score = 0 # 어피치 점수
    l_score = 0 # 라이언 점수
    lion_arr = [] # 라이언 화살
    # 중복 순열
    for lions in product(range(n), repeat=11):
        a_temp = 0 # 어피치 임시 점수
        l_temp = 0 # 라이언 임시 점수
        # n개의 화살 개수일 경우만 점수 계산
        if sum(lions) != n:
            continue
        for i, lion in enumerate(lions):
            # 라이언 화살수가 1보다 더 많은 경우는 건너뜀
            if lion-info[i] > 1:
                break
            # 둘 다 0일땐 점수 X
            if lion == 0 and info[i] == 0:
                continue
            # 라이언 화살 수가 1만큼 많으면 라이언 점수 획득
            if lion - info[i] == 1:
                l_temp += (10-i)
            elif lion <= info[i]: # 어피치 화살 수가 더 많거나 같으면 어피치 점수 획득
                a_temp += (10-i)
        # 라이언 점수가 어피치 점수보다 크고, 라이언과 어피치의 점수차가 더 큰 경우 갱신
        if l_temp > a_temp and l_temp-a_temp > l_score-a_score:
            l_score, a_score = l_temp, a_temp
            lion_arr = lions
            print(a_score, l_score, lion_arr)
    # 라이언이 이길 수 없는 경우(어피치 점수가 크거나 같은 경우)
    if a_score >= l_score:
        lion_arr = [-1]
    print(list(lion_arr))
    return list(lion_arr)

solution(5, [2,1,1,1,0,0,0,0,0,0,0]) # [0,2,2,0,1,0,0,0,0,0,0]
# solution(1, [1,0,0,0,0,0,0,0,0,0,0]) # [-1]
# solution(9, [0,0,1,2,0,1,1,1,1,1,1]) # [1,1,2,0,1,2,2,0,0,0,0]
# solution(10, [0,0,0,0,0,0,0,0,3,4,3]) # [1,1,1,1,1,1,1,1,0,0,2]