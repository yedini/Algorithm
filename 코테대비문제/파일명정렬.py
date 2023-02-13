def solution(files):
    answer = []
    for file in files:
        head = ''
        number = ''
        while file[0].isdigit() == False:
            head = head + file[0]
            file = file[1:]
            
        while file[0].isdigit():
            number = number + file[0]
            file = file[1:]
        
        answer.append([head, number, file])   # 여기서 file은 tail과 같음
    answer.sort(key = lambda x: (x[0].lower(), int(x[1])))
    answer = [file[0]+str(file[1])+file[2] for file in answer]
    return answer