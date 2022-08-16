# 첫번째 시도 : 타임아웃

# N = int(input()) # 1

# arr = list(map(int,input().split()))
# result=[]
# for i in range(0,N-1):
#     answer = -1
#     for j in range(i+1,N):
#         if arr[i]<arr[j]:
#             answer = arr[j]
#             break
#     result.append(str(answer))
# result.append(str(-1))

# print(" ".join(result))

# 2번째 풀이방식
# 배열의 인덱스를 스택에 저장하는 방식으로 접근

import sys
input = sys.stdin.readline
n = int(input())

arr = list(map(int,input().split()))
answer = [-1]*n
stack = []

stack.append(0)
for i in range(1,n):
    while stack and arr[stack[-1]]<arr[i]:
        answer[stack.pop()]=arr[i]
    stack.append(i)
for a in answer:
    print(a,end= " ")
# 뭔소리지... 인덱스르 스택에 넣는다?