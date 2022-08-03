N = int(input()) # 1

arr = list(map(int,input().split()))
result=[]
for i in range(0,N-1):
    answer = -1
    for j in range(i+1,N):
        if arr[i]<arr[j]:
            answer = arr[j]
            break
    result.append(str(answer))
result.append(str(-1))

print(" ".join(result))