# [프로그래머스] 양궁대회
# 참고: https://ye0nn.tistory.com/18
from itertools import combinations_with_replacement

def solution(n, info):
    # 어피치 점수판 정보
    a_info = info
    # 라이언 점수판 정보
    l_info = [-1]
    # 점수 차이 최대
    maxGap = -1e9
    # 중복 조합(화살 인덱스 조합)
    for lions in combinations_with_replacement(range(11), n):
        # 라이언 임시 점수판
        l_temp = [0]*11
        # 어피치, 라이언 점수
        a_score, l_score = 0, 0
        # 라이언 화살 개수 카운트(기존 최대 점수차와 현재 점수차가 같을 때, 낮은 점수 많은 것을 출력하기 위해 10-lion)
        for lion in lions:
            l_temp[10-lion] += 1 
        # 어피치, 라이언 점수 계산
        for i in range(11):
            if l_temp[i] > a_info[i]: # 어피치보다 라이언 화살이 더 많을 때만 라이언 점수
                l_score += (10 - i)
            elif l_temp[i] == 0 and a_info[i] == 0: # 둘 다 0이면 점수 미포함
                continue
            else: # 라이언보다 어피치 화살이 더 많거나 같은 개수면 어피치 점수
                a_score += (10 - i)
        # 라이언 점수가 더 크고, 라이언과 어피치 점수 차이 최대이면 maxGap, l_info 갱신
        if l_score > a_score and l_score-a_score > maxGap:
            maxGap = l_score-a_score
            l_info = l_temp
    return l_info

'''
아래 코드는 중복 순열을 활용한 풀이 방식이다. -> 0~n까지의 숫자를 길이 11 리스트에 차례로 조합하여 계산
정답이 도출되기는 하나, 시간이 매우 오래걸려 프로그래머스에서 시간초과가 발생한다.
본 문제에서는 중복 조합을 활용하여 시간을 단축시킬 수 있다. -> 0~10까지의 인덱스를 n개씩 조합하여 계산

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
    # 라이언이 이길 수 없는 경우(어피치 점수가 크거나 같은 경우)
    if a_score >= l_score:
        lion_arr = [-1]
    return list(lion_arr)
'''