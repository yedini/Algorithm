from itertools import permutations
def solution(n, weak, dist):
    l = len(weak)
    cand = []   # 수리가능한 친구 수 후보
    weak_point = weak + [w+n for w in weak]  # 선형으로 만들기!
    
    for i, start in enumerate(weak):
        for friends in permutations(dist):
            count = 1
            position = start     #취약점에서 시작 
            
            # 친구 조합 배치
            for friend in friends:
                position += friend
                # 끝 포인트까지 도달못할경우 친구 더 투입
                if position < weak_point[i+l-1]:
                    count += 1
                    # 현재 위치보다 멀리 있는 지점 중 가장 가까운 위치
                    position = [w for w in weak_point[i-1:i+l] if w > position][0]
                else:  # 끝 포인트까지 도달했을 때
                    cand.append(count)
                    break
    return min(cand) if cand else -1