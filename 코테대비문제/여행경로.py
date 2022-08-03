# 참고 1: https://velog.io/@inhwa1025/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-DFS
# 참고 2: https://gurumee92.tistory.com/165
from collections import defaultdict
def solution(tickets):
    answer = []
    # 시작점:도착점 그래프 생성
    graph = defaultdict(list)
    for (start, end) in tickets:
        graph[start].append(end)
        
    # 도착점 리스트 정렬: 알파벳 빠른 순으로 앞서는 경로를 가므로!
    for key in graph.keys():
        graph[key].sort()
        
    # ICN에서 출발
    stack = ['ICN']
    
    # dfs
    while stack:
        top = stack.pop()
        # top이 graph에 없거나 top을 시작점으로 하는 티켓이 없는 경우 answer에 저장
        if top not in graph or not graph[top]:
            answer.append(top)
        else: # 경로 있는 경우: 다시 스택에 넣고 도착점 중 알파벳이 빠른 지점을 스택에 저장
            stack.append(top)
            stack.append(graph[top].pop(0))
    return answer[::-1]