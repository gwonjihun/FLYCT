from itertools import permutations
num_list = ['0','1','1']

answer = 0
for i in range(1,len(num_list)+1):
    arr = []
    for j in permutations(num_list,i):
        print(j)
        if "".join(j) not in arr:
            arr.append("".join(j))
    for a in arr:
        print("-----------",a)
        tmp = int(a)
        for k in range(2, tmp):	# 2부터 x-1까지의 모든 숫자
            if tmp % k == 0:		# 나눠떨어지는게 하나라도 있으면 False
                break
            if k ==int(a)-1 :
                answer +=1
print(answer)