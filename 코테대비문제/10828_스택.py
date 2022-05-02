import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    codes = sys.stdin.readline().split()

    if codes[0] == 'push': 
        stack.append(codes[1])
    
    elif codes[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    
    elif codes[0] == 'size':
        print(len(stack))

    elif codes[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else: print(0)
    
    elif codes[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

