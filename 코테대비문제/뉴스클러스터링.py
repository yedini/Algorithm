from collections import Counter
def solution(str1, str2):

    # 두글자씩 끊어서 저장
    list1 = []
    for i in range(len(str1)-1):
        c = str1[i]+str1[i+1]
        if c.isalpha():
            list1.append(c.lower())
    
    list2 = []
    for i in range(len(str2)-1):
        c = str2[i]+str2[i+1]
        if c.isalpha():
            list2.append(c.lower())
    
    list1 = Counter(list1)
    list2 = Counter(list2)
    
    inter = list((list1 & list2).elements())
    union = list((list1 | list2).elements())
    
    if len(union) == 0:
        return 65536
    else: return int(len(inter)/len(union)*65536)