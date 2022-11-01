# https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91-Python
# Linked list 이용
def solution(n, k, cmd):
    cur = k  # 현재 위치
    # key는 열의 번호, value는 [prev 열, next 열]을 갖는 dict 생성
    table = {i:[i-1, i+1] for i in range(n)}
    answer = ['O']*n
    stack = []  # 삭제한 행 stack
    # 첫번째보다 앞, 마지막보다 뒤에는 없다고 표시
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    
    for c in cmd:
        # 삭제
        if c == 'C':
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])  # prev, now, next 저장
            
            # 현재 위치 수정
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            
            # prev node의 next항과 next node의 prev 항 수정
            if prev == None:
                table[next][0]=None
            elif next == None:
                table[prev][1]=None
            else:
                table[next][0] = prev
                table[prev][1] = next
        
        # 복구
        elif c == 'Z':
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now
        
        # 커서이동
        else:
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                # 현재 pointer가 다를 수 있으므로 단순히 cur에 더하면 안됨!
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
    return ''.join(answer)