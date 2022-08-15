import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)   # scoille을 heapq 형식으로 만들기  -> 값을 추가하면 자동 정렬
    while scoville[0] < K:    # 첫번째 값이 가장 작은 값이므로 첫번째 값이 K보다 작은지 확인
        # K 이상으로 못만드는 경우
        if len(scoville) <=1 or answer >= K:
            return -1
        n = heapq.heappop(scoville)
        n2 = heapq.heappop(scoville)
        heapq.heappush(scoville, n + n2*2)
        answer += 1