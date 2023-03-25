import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # 가장 작은 값이 K보다 커질때까지 / 더 합칠 수 없을 때까지(scoville에 남은 원소가 1개) while문을 실행
    while scoville[0] < K and len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer += 1
    return answer if scoville[0] >= K else -1  # scoville에 남은 1개의 원소가 K보다 작으면 실패 --> -1 출력