from itertools import *

def solution(orders, course):
    result = {}
    for order in orders:
        # combinations을 사용하기 위한 전제조건(입력으로 들어온 데이터의 정렬)
        order = sorted(order)
        order = "".join(order)
        for num in course:
            # 여기서 중요한 점은 permutations가 아닌 combinations를 사용하는 것이다.
            # 아무리 브루트 포스 문제라고 해도, permutations는 중복 가능한 모든 값을 찾아내기 때문에 시간초과가 뜬다.
            for output in list(combinations(order, num)):
                data = "".join(list(output))
                if data not in result:
                    result[data] = 1
                else:
                    result[data] += 1
    answer = []
    for num in course:
        max_value = 0
        max_key = []
        for k, v in result.items():
            if len(k) == num:
                if max_value < v:
                    max_value = v
                    max_key = []
                    max_key.append(k)
                elif max_value == v:
                    max_key.append(k)
        buf = ""
        for s in max_key:
            s = sorted(s)
            if buf != "".join(s):
                buf = "".join(s)
            else:
                continue
            if buf not in answer:
                if max_value != 1:
                    answer.append(buf)
    answer.sort()
    return answer