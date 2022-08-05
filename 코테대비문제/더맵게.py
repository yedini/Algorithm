import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <=1 or answer >= K:
            return -1
        n = heapq.heappop(scoville)
        n2 = heapq.heappop(scoville)
        heapq.heappush(scoville, n + n2*2)
        answer += 1