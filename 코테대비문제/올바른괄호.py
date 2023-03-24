def solution(s):
    stack = []
    for i in s:
        if i == '(':     # ( 일 경우 
            stack.append(i)
        else:
            if len(stack) == 0:  # stack이 비어있는데 )가 나온 경우 -> 올바르지 않음
                return False
            else:  # stack에 (가 있고 다음으로 )가 온 상태 ->
                stack.pop()
    return len(stack) == 0