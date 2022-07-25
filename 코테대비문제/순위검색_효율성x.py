from copy import deepcopy
def solution(info, query):
    answer = []
    info = [i.split() for i in info] # 한 information별로 단어가 끊어져 있는 리스트로 만들기
    for i in range(len(query)):
        temp = deepcopy(info)
        q = query[i].replace('and ', '').split() # query도 info랑 같은 형태로
        for j in q[:-1]:
            if j == '-':  # - 면 고려 x
                continue
            else:
                temp = [l for l in temp if j in l]  # 같은게 해당되면 temp에 남고 아니면 제외
        temp = [l for l in temp if int(l[-1]) >= int(q[-1])] # score가 query 이상이면 남고 아니면 제외
        answer.append(len(temp)) 
    return answer