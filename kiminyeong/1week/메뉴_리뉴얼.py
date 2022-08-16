# [프로그래머스] 메뉴 리뉴얼
'''
문제
각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, 
"스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, 
"스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

제한사항
1. orders 배열의 크기는 2 이상 20 이하입니다.
2. orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
    각 문자열은 알파벳 대문자로만 이루어져 있습니다.
    각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
3. course 배열의 크기는 1 이상 10 이하입니다.
    course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
    course 배열에는 같은 값이 중복해서 들어있지 않습니다.
4. 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
    배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
    만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
    orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.
'''

from itertools import combinations

def solution(orders, course):
    answer = []
    # 코스 개수
    for c in course:
        # 메뉴 구성 count용 딕셔너리
        menu_dic = dict()
        for order in orders:
            # 조합을 사용하여 중복 없는 모든 메뉴(경우의 수)
            for menu in combinations(order, c):
                # 각 경우의 수를 정렬하여 문자열로 변환
                menu = ''.join(sorted(list(menu)))
                # menu_dic에 이미 있는 메뉴면 카운트
                if menu in menu_dic:
                    menu_dic[menu] += 1
                else:
                    menu_dic[menu] = 1

        # 가장 많이 주문한 메뉴 구성 찾기 (2번 이상 주문)
        for m in menu_dic:
            # 최대 주문 수
            menu_max = menu_dic[max(menu_dic, key = menu_dic.get)]
            # 최대 주문 수 이면서 2번 이상 주문된 메뉴 구성
            if menu_dic[m] == menu_max and menu_dic[m] >=2:
                answer.append(m)
    return sorted(answer) # 메뉴 구성을 오름차순으로 정렬