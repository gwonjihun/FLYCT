# Author. K9714
# Date. 22.07.29
# Programmers. 메뉴 리뉴얼

# Python Version
# 3.8.9

# 조건
# 1. 손님들이 주문한 주문 배열 orders 주어짐
# 2. 세트 메뉴를 만들고자 하는 세트 조합 개수 배열 course 주어짐
# 3. orders 의 길이는 2 이상 20 이하
# 4. orders 요소의 길이는 2 이상 10 이하
# 5. orders 요소는 모두 알파벳 대문자의 조합으로 구성되어있으며, 중복은 없음
# 6. course 의 길이는 2 이상 10 이하
# 7. course 요소는 2 이상 10 이하의 자연수로, 오름차순 정렬되어 중복은 없음

# 목표
# 1. orders 배열의 주문정보를 통한 course 배열의 메뉴 개수로 가장 주문 빈도 높은 세트메뉴를 출력
# 2. 세트메뉴 구성 및 출력은 모두 사전 정렬 기준으로 출력되어야 함
#---------------------------

from itertools import *
from collections import Counter

def solution(orders, course):
    # 최고 메뉴 개수를 구하기 위한 딕셔너리 생성
    menus = {}
    answer = []
    # 원하는 메뉴 수로 분기
    for c in course:
        # 메뉴 수를 key 로 하는 배열 생성
        menus[c] = []
        for order in orders:
            # 단어 사전 순서대로 재배열
            sort_word = ''.join(sorted(order, key=str.lower))
            # 단어에 대한 조합(combination) 생성
            comb = list(combinations(sort, c))
            # 조합 출력 파싱 => ('A', 'B'), ('A', 'C') 형식을 AB, AC 로 이어붙임
            for m in comb:
                menus[c].append("".join(m))
        # 현재 메뉴 조합에서 가장 빈도가 높은 순서대로 정렬
        max_menu = Counter(menus[c]).most_common()
        # 조합 조건을 만족하는 메뉴가 있는지 검사
        if len(max_menu) != 0:
            # 가장 높은 빈도수 측정
            max_value = max_menu[0][1]
            # 최소 빈도가 2 이상인 경우만 카운팅
            if max_value > 1:
                # 중복 빈도 필터링
                all_menu = list(filter(lambda x: x[1] == max_value, max_menu))
                all_menu = list(map(lambda x: x[0], all_menu))
                # 최종 선정된 빈도수의 메뉴를 출력 배열에 concat
                answer = answer + all_menu

    # 사전 순서대로 배치
    answer.sort()
    return answer
