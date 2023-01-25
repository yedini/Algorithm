def solution(record):
    answer = []
    action = []
    users = dict()
    for r in record:
        user = r.split(" ")
        action.append([user[0], user[1]])
        if user[0] in ['Enter', 'Change']:
            users[user[1]] = user[2]
            
    for a in action:
        if a[0] == 'Enter':
            answer.append(users[a[1]]+"님이 들어왔습니다.")
        elif a[0] == 'Leave':
            answer.append(users[a[1]]+"님이 나갔습니다.")
            
    return answer