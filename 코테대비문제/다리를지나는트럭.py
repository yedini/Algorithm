def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    bridge_sum = 0
    
    while bridge:
        temp = bridge.pop(0)
        bridge_sum -= temp
        answer += 1
        
        if truck_weights:
            if bridge_sum + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
                bridge_sum += t
            
            else:
                bridge.append(0)
    
    return answer