# 원소 개수 적은 순서로 정렬
# 원소개수 하나인 튜플의 숫자를 answer로 가져오기
# 다음 튜플과 현재 answer의 차집합을 answer에 추가

def solution(s):
    answer = []
    tuples=[]
    temp = ''
    # 문자열로 주어진 숫자를 한 튜플마다 끊어서 tuples 안에 리스트로 저장
    for i in s:
        if i == "}":
            temp = temp.replace("{", "")
            tuples.append([x for x in temp.split(",") if x != ""])   
            temp = ''
        else:
            temp = temp + i
            
    # 튜플의 크기 순으로 정렬
    tuples = sorted(tuples, key = lambda x: len(x))
    
    # answer와의 차집합을 구해서 다음 원소를 answer에 추가
    for t in tuples[1:]:
        new = set(list(map(int, t))) - set(answer)
        answer.append(list(new)[0])
    return answer