def solution(s):
    answer = 0
    for _ in range(len(s)):
        stack = []
        temp = True
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            else:
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                elif stack[-1] == '[' and i == ']':
                    stack.pop()
                else: 
                    stack.append(i)
        if len(stack) == 0:
            answer += 1
        
        s = s[1:] + s[0]
    return answer