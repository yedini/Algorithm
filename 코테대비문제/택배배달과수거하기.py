def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0
    pickup = 0
    # 배달, 수거 리스트 거꾸로 뒤집기
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    for i in range(n):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while delivery > 0 or pickup > 0 :
            delivery -= cap
            pickup -= cap
            answer += (n-i)*2 # 왕복
    return answer