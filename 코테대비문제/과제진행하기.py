# 제시간에 해야될 과제 하고 시간 남았을 때 남은 과제 하는 함수
def check_others(plans, others, t):   # plans, 남은 과제들, 남은 시간
    adds = [] # answer에 추가될 과제 이름
    while t>0 and others:
        x = others.pop()  # 제일 최근 거 이어서 하기
        if x[1] > t:  # 남은 시간에 다 못끝냄 -> 다시 others에 집어넣기
            others.append((x[0], x[1]-t))
            t = 0
        else:
            adds.append(x[0])
            t -= x[1]

    return others, adds
    

def solution(plans):
    answer = []
    
    # 과제 시작시간: 한시간을 60분으로 바꾸고 수치화 / 과제 소요 시간: 수치화
    for i in range(len(plans)):
        temp = plans[i][1].split(":")
        plans[i][1] = int(temp[0])*60+int(temp[1])
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key = lambda x: x[1])   # 과제 시작 시간 순으로 정렬

    others = []
    for i in range(len(plans)-1):
        pos = plans[i+1][1] - plans[i][1]    # 다음 과제 시작 시간까지 가능한 시간
        
        #시간이 모자라는 경우: 모자라는 시간 만큼 others에 추가
        if pos < plans[i][2]:
            others.append((plans[i][0], plans[i][2]-pos))
        
        # 시간 내에 할 수 있는 경우
        else:
            answer.append(plans[i][0])
            # 시간이 남는 경우: 남는 시간에 앞에서 못한 과제 추가로 하기
            if pos > plans[i][2]:
                others, adds = check_others(plans, others, pos-plans[i][2])
                answer = answer + adds  # 새롭게 끝낸 과제가 있다면 answer에 추가하기
    
    # 시간상 마지막 과제는 시간제한이 없으므로 바로 answer에 추가
    answer.append(plans[-1][0])
    
    # 아직 다 못끝낸 과제들: 가장 최근에 하다 멈춘 과제부터 순서대로 끝내기
    if len(others)>0:
        answer = answer + [others[i][0] for i in range(len(others)-1, -1, -1)]
        
    return answer