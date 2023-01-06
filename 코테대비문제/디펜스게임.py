from heapq import heappop, heappush  
def solution(n, k, enemy):
    answer = 0
    sum_e = 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)  # heappush는 최소힙이므로, -를 붙여 최대힙으로 사용함
        sum_e += e   # 적의 전체 수에 현재 적의 수 e를 누적으로 더함
        if sum_e > n: # 적의 전체 수가 병사 수 n보다 많을 경우
            if k == 0:  # 무적권도 존재하지 않을 경우 더이상 진행 x
                break
            # 지금까지 추가한 수 중 가장 큰 원소값만큼 sum에서 빼고, k도 차감    
            sum_e += heappop(heap)  
            k -= 1
        answer += 1
    
    return answer