def solution(lottos, win_nums):
    answer = []
    return answer
answer =[]
lottos =    [44, 1, 0, 0, 31, 25]
win_nums=	[31, 10, 45, 1, 6, 19]

zero = 0
suc = 0
for i, data in enumerate(lottos):
    if data in win_nums:
        suc+=1
    if data == 0 :
        zero +=1
if zero == 0 and suc ==0:
    answer.append("6")
else:
    answer.append(str(6-zero-suc+1))

if suc<2:
    answer.append("6")
else:
    answer.append(str(7-suc))

print(" ".join(answer))