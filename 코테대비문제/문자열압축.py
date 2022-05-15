'''
같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현
-> 더 짧은 문자열로 줄여서 표현하자
-> 문자열을 1개 이상의 단위로 잘라 압축해서 더 짧게 표현할 수 있는지 찾자
-> 가장 짧게 표현했을 때 그 때의 길이를 구하자

n개 단위로 자르고 마지막에 남으면 그건 그대로 붙여주기.

ex. "ababcdcdababcdcd" 문자열을
1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 자르면 "2ab2cd2ab2cd"로 표현 가능함.
8개 단위일 때 "2ababcdcd" 로 가장 짧다.
'''
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1): # 문자열을 자를 단위
        result = ''  # i개 단위로 자를 때의 압축결과
        temp = ''    # 이전 단계에서 잘라진 문자열
        templ = 1    # 이전 단계의 문자열이 나온 횟수
        for j in range(len(s)//i):   # i개단위로 자를 때 자를 수 있는 횟수
            now = s[i*j:i*(j+1)]     # 현재 확인하는 문자열
            if now == temp:          # 이전 단계와 똑같을 경우 -> 횟수 +1
                templ += 1
            else:                    # 앞의 문자열과 다른 문자열일 때
                if templ >= 2:       # 앞의 문자열이 쌓인 횟수가 2번 이상일 때
                    result = result + str(templ) # 쌓인 횟수만큼을 result에 추가
                    templ = 1        # 현재 단계의 문자열은 처음 나온거니까 횟수 초기화
                result = result + now   # 현 단계에서 새로 확인한 문자열을 result에 추가
                temp = now              # temp update

        # 나눌 수 있는 만큼까지 다 나누고 고려해야할 요소

        # templ>=2일 때: templ까지 result에 반영되어야 하는데 아직 안된 상태 -> 반영하기
        if templ >= 2:
            result = result + str(templ)
        
        # i개 단위로 문자열 나눴을 때 남는 문자열이 있는 경우 -> result에 추가
        if len(s)%i >= 1:
            result = result + str(s[-(len(s)%i):])

        # 현재 최소 길이보다 짧을 경우 answer update
        if len(result) < answer:
            answer = len(result)
    return answer