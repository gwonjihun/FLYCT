def solution(phone_book):
    answer = True
    for i in range(0,len(phone_book)):
        for j in range(i+1,len(phone_book)):
            a = len(phone_book[i])
            b = len(phone_book[j])
            if a >= b:
                if phone_book[i][:b]==phone_book[j][:b]:
                    answer= False
            else:
                if phone_book[i][:a]==phone_book[j][:a]:
                    answer= False
    return answer
# a 랑 b랑 비교를 해야하는데
# 1. a b 의 길이를 비교
# 2. if else로 a>b , b=<a를 결정
# 3. phone_book[len(a)]
#answer = ['123','1234']
#print(answer[0][:]==answer[1][:3])
#result : true

# 정확도 : 41.7
# 효율성 : 0...