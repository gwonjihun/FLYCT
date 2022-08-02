from itertools import *

def solution(orders, course):
    result = {}
    for order in orders:
        for num in course:
            for output in list(permutations(order, num)):
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