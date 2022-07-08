def solution(progresses, speeds):
    answer = []
    count = []  # 각 기능마다 필요한 작업 횟수
    
    # 각 기능별로 필요한 작업일을 count에 담음
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] != 0:  #나머지가 있는 경우 -> 한번 더 더해줘야 함
            count.append((100-progresses[i]) // speeds[i] + 1)
        else:
            count.append((100-progresses[i]) // speeds[i])

    # 모든 작업이 배포될 때까지 반복        
    while len(count) > 0 :
        n = count.pop(0) # 가장 앞에 있는 기능의 작업일을 꺼냄
        # 더 남아있는 기능이 없는 경우 방금 꺼낸 n이 유일하게 배포됨 -> answer에 1 추가
        if len(count) == 0: 
            answer.append(1)
        else:
            c = 1  # 같이 배포되는 기능의 개수
            # count에 남아있는 모든 작업일에 첫번째 기능의 작업일(=n)을 빼줌
            count = [i-n for i in count] 
            # 남은 coun의 첫번째 수가 음수 -> 앞에서 뺀 기능보다 먼저 끝난 것 -> 빼주고 c +=1
            while len(count)>0 and count[0] <= 0 :
                _ = count.pop(0)
                c += 1
            answer.append(c)
    return answer