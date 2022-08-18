n, weight = map(int, input().split())
arr = [(0, 0)]

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

dp = [[0]*(weight+1) for _ in range(n+1)] # dp생성
#  i는 비교를 위해 선택된 물체
# j는 현재 가방에서 활용될 수 있는 무게
for i in range(1, n+1):
    tmp_w, tmp_v = arr[i][0], arr[i][1]
    for j in range(1, weight+1):
        
        if j < tmp_w:
            dp[i][j] = dp[i-1][j]
            print("@@@@@@@@@@@@@@@@@@@@ 1")
        else:
            dp[i][j] = max(dp[i-1][j-tmp_w]+tmp_v, dp[i-1][j]) #해당 문장을 통해서 최대 효율 추출
            print("################################## 2")
        print("i :", i,"j" ,j,"Temp_w",tmp_w,dp)
        print("------------------------------------------------------------------------")

print(dp[-1][-1])