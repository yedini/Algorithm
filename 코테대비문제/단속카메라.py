def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])  # 진출 지점 기준으로 정렬
    now = routes[0][1] # 가장 첫번째 차량의 진출 지점에 카메라 하나 설치
    answer += 1
    
    for i in range(1, len(routes)):
        # 다음 차량이 카메라 설치 지점 이후에 들어오면 해당 차량의 진출 지점에 새로운 카메라 설치
        if now < routes[i][0]: 
            answer += 1
            now = routes[i][1]
    return answer