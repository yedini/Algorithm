def solution(dirs):
    visited = set()   # 처음 걸어본 길의 개수를 세기 위한 set
    visited_all = set()  # 처음 걸어간 방향과 반대로 걸어간 방향을 모두 포함
    now = [0, 0]
    move = {'U':[0, 1], 'D':[0, -1], 'R':[1, 0], 'L':[-1, 0]}  # 이동 방향에 따른 dictionary
    for d in dirs:
        m = move[d]

        if -5<=now[0]+m[0]<=5 and -5<=now[1]+m[1]<=5:
            new = [now[0]+m[0], now[1]+m[1]]
            
            # 현재 좌표와 새 좌표를 string으로 이어붙여 visited에 저장
            # 반대방향으로 가는 것도 고려하기 위해, 
            # visited에는 현재 방향만 저장하고 visited all에는 양방향을 모두 저장함
            route = ''.join([str(now[0]), str(now[1]), str(new[0]), str(new[1])])
            route_reverse = ''.join([str(new[0]), str(new[1]), str(now[0]), str(now[1])])

            if (route not in visited_all) and (route_reverse not in visited_all):
                visited.add(route)
                visited_all.add(route)
                visited_all.add(route_reverse)
        now = new

    return len(visited)