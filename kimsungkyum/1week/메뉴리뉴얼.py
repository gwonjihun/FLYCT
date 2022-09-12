from itertools import combinations
from collections import Counter

def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    print(order)
    if order:
        maximum = order[0][1]

    modes = []
    for num in order:
        print(num[1])
        if num[1] == maximum and num[1] > 1:
            modes.append(''.join(num[0]))
    return modes

def solution(orders, course):
    answer = []
    
    for i in course:
        l = [] 
        for j in orders:
#            print(list(map(''.join, combinations(j,i))))
            temp = list(combinations(j,i))
            for i in temp:
                i
            for i in 
            l = l+list(list(map(''.join, combinations(j,i))))
            print(l)
            l.sort()
        answer += modefinder(l)
    
    answer.sort(key = str.lower)
    print(answer)
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4] 

solution(orders, course)
