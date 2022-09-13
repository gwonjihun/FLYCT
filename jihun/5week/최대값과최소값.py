def solution(s):
    split_s = s.split(" ")
    split_s = list(map(int, split_s))
    max_S = max(split_s)
    min_S = min(split_s)
    answer = ' '.join(list(map(str,[min_S,max_S])))
    return answer


print(solution("-1 -2 -3 -4"))