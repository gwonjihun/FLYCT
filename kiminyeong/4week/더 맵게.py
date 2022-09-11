# [프로그래머스] 더 맵게
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while 1:
        # 가장 맵지 않은 음식의 스코빌 지수
        one = heapq.heappop(scoville)
        # 모든 음식이 K 이상일 경우 종료
        if one >= K:
            break
        # 스코빌 지수로 만들 수 없는 경우 -1
        if len(scoville) == 0:
            return -1
        # 두번째로 맵지 않은 음식의 스코빌 지수
        two = heapq.heappop(scoville)
        # 섞은 음식의 스코빌 지수
        mix = one + (two * 2)
        # 힙에 다시 추가
        heapq.heappush(scoville, mix)
        count += 1
    
    # 모든 음식의 스코빌 점수가 K 이상이 되도록 섞은 횟수
    return count

print(solution([1, 2, 3, 9, 10, 12], 7))