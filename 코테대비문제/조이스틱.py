#https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
def solution(name):
    answer = 0
    # 좌우 이동의 최소 횟수: 길이 -1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
        # 상하로 움직이는 최소값을 answer에 추가
        answer += min(ord(char)-ord('A'), ord('Z')-ord(char)+1)
        
        # 연속된 A가 있는 구간은 안가는게 효율적->해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 좌우 움직임 업데이트: 기존/연속 A의 왼쪽에서 시작/연속 A의 오른쪽에서 시작
        min_move = min([min_move, 2*i+len(name)-next, i+2*(len(name)-next)])
    
    answer += min_move
    return answer