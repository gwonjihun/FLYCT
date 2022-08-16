n, K = map(int,input().split())

inputs = list(input())
# 햄버거를 먹으면 1을 0으로
# 버거를 먹으면 reseult 1++를 진행
# #
answer = 0
for s in range(0,n):
    #print(inputs[s]=='P')
    if inputs[s]=='P':
        for i in range(max(s-K,0),min(s+K+1,n)):
            if inputs[i]=='H':
                inputs[i]='0'
          #      print(inputs[i])
                answer += 1
                break
print(answer)