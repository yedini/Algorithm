def solution(weights):
    answer = 0
    # 동일위치 제외하고 앉을 수 있는 위치 조합
    positions = [(2,3), (2,4), (3,4), (4,3), (4,2), (3,2)]
    
    # 각 weight별 사람 수를 count하는 dict 자료형 생성
    wmap = {}
    for w in weights:
        # setdefault 함수: index 없을 경우 defaultdict 생성
        wmap.setdefault(w, 0)
        wmap[w] += 1
    
    for weight in wmap:
        wcount = wmap[weight]
        # 무게가 같은 사람이 2명 이상 -> 서로 같은 자리에 앉을 수 있음
        # 이 때 만들 수 있는 조합의 수는 nC2
        if wcount > 1:
            answer += wcount * (wcount-1) // 2
        
        # 다른 사람과 각 position에 앉았을 때 짝꿍이 될 수 있는지 확인
        for (me, friend) in positions:
            # 무게: x, y 위치: a,b라고 할 때 평형이면 y = x * a / b
            friend_weight = weight*me/friend
            if friend_weight in wmap:
                answer += wcount*wmap[friend_weight]
        # 중복 방지: 계산을 끝낸 몸무게는 제거
        wmap[weight] = 0
    return answer