def solution(n, arr1, arr2):
    answer = []
    list1 = []
    list2 = []
    for i in range(n):
        n1 = format(arr1[i], 'b')
        while len(n1) < n:
            n1 = '0'+n1
        n2 = format(arr2[i], 'b')
        while len(n2) < n:
            n2 = '0'+n2
            
        list1.append(n1)
        list2.append(n2)
        
        ans = ''
        for j in range(n):
            if int(list1[i][j]) + int(list2[i][j]) >=1:
                ans = ans + '#'
            else:
                ans = ans + ' '
        answer.append(ans)
        
    return answer