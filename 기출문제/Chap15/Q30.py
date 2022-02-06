from bisect import bisect_left, bisect_right

# 값이 left_value, right_value 사이에 있는 데이터의 개수 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 단어를 길이별로 나누어 저장할 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이별로 뒤집어 저장할 리스트(접두가 ?인 경우에 대비)
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    # array, reversed_array에 각각 넣기
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1]) #뒤집기!
        
    # 길이별 리스트마다 정렬! (이진탐색 수행을 위해)
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    # 쿼리별로 처리
    for q in queries:
        if q[0] != '?':  # 첫번째가 ?가 아님
            # 입력된 문자들 포함 처음부터 끝까지 -> ?가 다 a일 때부터 다 z일 때 까지 확인.. 대박
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:  # 접두사가 ? => 뒤집어서 보자
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 검색된 단어 개수 저장
        answer.append(res)
    return answer