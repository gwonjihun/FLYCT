def solution(record):
    dic = {} # 키== id item = 닉네임
    for a in record:
        arr = a.split(" ")
        if arr[0] == "Enter":
            if a[1] in dic.keys():
                dic[a[1]]= a[2]
                
            else:
                dic[a[1]] = a[2]

    answer = []
    
    return answer
