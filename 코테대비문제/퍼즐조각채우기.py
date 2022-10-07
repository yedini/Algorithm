import copy

def dfs(gb, x, y, position, n, num):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ret = [position]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and gb[nx][ny] == num:
            gb[nx][ny] = 2
            ret = ret + dfs(gb, nx, ny, [position[0]+dx[i], position[1]+dy[i]], n, num)
    return ret

def rotate(table):
    n = len(table)
    ret = [[0]* n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = table[i][j]
    return ret

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    gb_copy = copy.deepcopy(game_board)
    block = []  # 기존 게임보드에서 빈칸 묶음으로 파악
    for i in range(n):
        for j in range(n):
            if gb_copy[i][j] == 0:
                gb_copy[i][j] = 2
                result = dfs(gb_copy, i, j, [0,0], n, 0)[1:]
                block.append(result)
                
    for r in range(4):
        table = rotate(table)
        tr_copy = copy.deepcopy(table)
        
        for i in range(n):
            for j in range(n):
                if tr_copy[i][j] == 1:
                    tr_copy[i][j] = 2
                    result = dfs(tr_copy, i, j, [0, 0], n, 1)[1:]
                    
                    if result in block:  
                        block.pop(block.index(result))
                        answer += (len(result)+1)
                        table = copy.deepcopy(tr_copy)
                    else:
                        tr_copy = copy.deepcopy(table)
    return answer