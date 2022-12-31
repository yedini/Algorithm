def solution(info, edges):
    answer = []
    visited = [0]*len(info)
    visited[0] = 1
    
    def dfs(sheep, wolf):  # 양 수, 늑대 수
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            ws = info[child]  # 양 또는 늑대
            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep+(ws==0), wolf+(ws==1))
                visited[child] = 0
    dfs(1, 0)
    return max(answer)