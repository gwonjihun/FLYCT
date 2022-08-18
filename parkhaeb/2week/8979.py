N, K = map(int, (input().split()))
m = [list(map(int, (input().split()))) for _ in range(N)]

s = sorted(m, key = lambda x : (-x[1], -x[2], -x[3])) # 익명함수 사용하여 메달 순서대로 정렬

# 등수 알고 싶은 국가의 인덱스 찾기
for i in range(N) :
    if s[i][0] == K :
        index = i

# 메달의 수가 같은 경우 (등수가 겹치는 경우) 등수는 인덱스+1이므로 출력해줌
for i in range(N) :
    if s[index][1:] == s[i][1:] :
        print(i+1)
        break

# for문 하나에 두 개의 if문을 사용했을 때, 런타임 에러 뜸!