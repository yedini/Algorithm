from itertools import product
def solution(word):
    words = []
    for i in range(1, 6): #1글자부터 5글자까지 가능
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i): # size=i인 cartesian product
            words.append(''.join(list(j)))
    
    words.sort()
    answer = words.index(word)+1  #알고자하는 단어의 순서 출력
    return answer