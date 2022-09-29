def solution(info, edges):
    answer = []
    visited = [0]*len(info)    
    visited[0] = 1
    
    def dfs(sheep, wolf):
        # 한칸 더 갔을 때 양이 늑대보다 많으면 정답 후보에 추가
        if sheep > wolf:
            answer.append(sheep)
        # 늑대가 많으면 끝
        else:
            return
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            ws = info[child]
            # 방문하지 않은 자식 노드인 경우 들어갔다 나오기
            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep+(ws==0), wolf+(ws==1))
                visited[child] = 0
    dfs(1, 0)
    return max(answer)