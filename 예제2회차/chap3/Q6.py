import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i))  # (걸리는 시간, 인덱스)
    
    count = 0  # 지나간 시간
    complete = 0 # 이전에 먹은 음식 시간 합 
    length = len(food_times)  # 남은 음식 개수
    
    # 다음 음식 다먹었을 때 시간이 k보다 작거나 같은 경우
    while count + (heap[0][0]-complete)*length <= k:
        minf = heapq.heappop(heap)[0]    # 새로 다먹을 음식이니까 남은 리스트에서 꺼내기
        count += (minf - complete)*length # 추가로 소요되는 시간*남은 음식개수
        complete = minf  # 음식 먹는데 걸린 시간 업데이트
        length -= 1      # 음식 하나 줄었으니까 길이 -1
                 
    # 처음 인덱스에 맞춰 돌아가니까 인덱스 기준으로 정렬
    heap = sorted(heap, key = lambda x: x[1]) 
    # 남은 음식 길이가 중단되기까지 걸리는 시간보다 짧으면 2바퀴 이상 돌 수도 있음
    # => 나눴을 때 나머지값이 정답
    return heap[(k-count)%length][1]+1    


print(solution([3, 1, 2], 5))