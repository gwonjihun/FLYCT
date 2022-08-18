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