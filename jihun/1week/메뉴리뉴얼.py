from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    # 메뉴의 입력된 값들에 따른 조합들을 만들기
    # 1. 먼저 order에 대한 조합을 만들어줘야함
    # recruit함수를 사용한다면? 
    for cour in course:
        course_order = []
        # course_order : 코스의 요리 가지 수
        for ordr in orders:
            for combi in combinations(ordr,cour):
                course_order.append(''.join(sorted(combi)))
        print(str(cour)+"개 코스는: ", course_order)
        #위에서는 각 코스마다 가능한 조합을 배열로 저장
        #아레부터는 각 코스 조합이 주문되었던 갯수를 카운트 해준다.
        print("----------------------")
        course_order = Counter(course_order).most_common()
        print(course_order)
        max = 0
        for ans in range(0,len(course_order)):
            if ans==0:
                max = course_order[ans][1]
            if course_order[ans][1]==max and course_order[ans][1]>1:
                answer.append(course_order[ans][0])
        
        answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"] ,[2,3,4]))