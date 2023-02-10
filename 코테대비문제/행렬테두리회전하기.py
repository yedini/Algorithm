def solution(rows, columns, queries):
    answer = []
    graph = [list(range(1+i*columns, columns+i*columns+1)) for i in range(rows)]
    
    for query in queries:
        x1, y1, x2, y2 = query
        x1 -=1 ; y1 -=1 ; x2 -=1 ; y2 -=1 ; 
        minnum = 10e9
        
        # 처음 값 저장
        temp = graph[x1][y1]
        
        # 왼쪽
        for j in range(x1, x2):
                og = graph[j+1][y1]
                minnum = min(minnum, og)
                graph[j][y1] = og
        
        # 아래쪽
        for j in range(y1, y2):
                og = graph[x2][j+1]
                minnum = min(minnum, og)
                graph[x2][j] = og
        
        # 오른쪽
        for j in range(x2, x1, -1):
                og = graph[j-1][y2]
                minnum = min(minnum, og)
                graph[j][y2] = og
        
        # 위쪽
        for j in range(y2, y1, -1):
                og = graph[x1][j-1]
                minnum = min(minnum, og)
                graph[x1][j] = og
                
        graph[x1][y1+1] = temp
        minnum = min(minnum, temp)
        
        answer.append(minnum)
    return answer