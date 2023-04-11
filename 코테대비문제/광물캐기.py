# 가지고 있는 곡괭이로 확인 가능한 광물까지 5개 단위로 잘라서 출력하는 함수
def mineral_prev(minerals, picks):
    new = [minerals[i:i+5] for i in range(0, sum(picks)*5, 5)]
    # diamond, iron 적은 순으로 정렬
    new.sort(key = lambda x: (sum([i=="diamond" for i in x]), sum([i=="iron" for i in x])))
    return new

def solution(picks, minerals):
    answer = 0
    graph = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]  # 곡괭이 종류 별 피로도
    
    # 제시된 minerals를 5개씩 자르고 정렬
    minerals = mineral_prev(minerals, picks)
    pnow = 0  # 현재 곡괭이 종류
    
    while minerals and picks:
        # 입출력 예 2와 같이 곡괭이 종류가 0개인게 앞에 있을 경우 빼주기
        while picks[0] == 0:
            picks.pop(0)
            pnow += 1
        
        # 5개 단위로 잘린 광물 중 한단위 빼오기 - diamond, iron이 많은 순으로 
        m = minerals.pop()
        
        # 현재 곡괭이 종류에 맞는 피로도 계산
        answer += sum([graph[pnow][0] if m[j]=='diamond' else graph[pnow][1] if m[j]=='iron' else graph[pnow][2] for j in range(len(m))])
        
        # 곡괭이 하나 5번 사용했으므로 빼주기
        picks[0] -= 1
        
        # 한 종류의 곡괭이를 다 쓴 경우 picks 리스트에서 빼기
        if picks[0] == 0:
            picks.pop(0)
            pnow += 1
    

    return answer