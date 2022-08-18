'''
그룹 단어 체커

'''

# 입력받는 시간 줄이기
import sys
input = sys.stdin.readline

# 들어올 데이터 갯수 받아오기
N = int(input().strip())

# 들어올 데이터 개수만큼 count 지정
count = N

# 들어온 데이터 개수 만큼 반복
for _ in range(N):
    # 비교를 위한 리스트 선언
    buffer = []

    # 들어온 데이터 리스트로 각각 저장
    words = list(map(str, input().strip()))

    # 들어온 데이터 파싱해서 그룹 단어인지 체크
    for idx, word in enumerate(words):
        if idx == 0:
            buffer.append([word])
        elif [word] in buffer:
            if buffer[-1] != [word]:
                # 만약 들어온 데이터가 이전에 들어왔던 데이터이고, 바로 전에 들어왔던 데이터가 아니라면 count 빼주기
                count -= 1
                break
            else:
                buffer.append([word])
        else:
            buffer.append([word])
print(count)
