from itertools import permutations
def solution(user_id, banned_id):
    answer = []
    cand = list(permutations(user_id, len(banned_id)))
    
    for c in cand:
        if_c = True
        for i in range(len(c)):
            # 같은 길이의 문자인지 확인
            if len(c[i]) != len(banned_id[i]):
                if_c = False
            # *가 아닌 문자가 같은 문자인지 확인
            else:
                temp = [False if (banned_id[i][j] == '*' or c[i][j] == banned_id[i][j]) else True for j in range(len(c[i]))]
                if sum(temp) >0:
                    if_c = False
        if if_c and set(c) not in answer:
            answer.append(set(c))
    return len(answer)