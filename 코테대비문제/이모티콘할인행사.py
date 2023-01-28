from itertools import product
def solution(users, emoticons):
    answer = []
    sales = [10, 20, 30, 40]
    slist = list(product(sales, repeat=len(emoticons)))
    
    for sales in slist:
        join_count = 0
        purchase = 0
        for user in users:
            user_e_sum = int(sum([emoticons[i]*(1-sales[i]*0.01) for i in range(len(sales)) if sales[i]>=user[0] ]))
            if user_e_sum >= user[1]:
                join_count += 1
            else:
                purchase += user_e_sum
                
        answer.append([join_count, purchase])
        
    answer.sort(key = lambda x: (x[0], x[1]))
    
    return answer[-1]