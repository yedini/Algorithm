import heapq  # 우선순위 큐 활융: 힙 자료구조
N = int(input())

heap = []
for i in range(N):
    heapq.heappush(heap, int(input()))

result=0

# heap에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 묶음 2개 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one+two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)