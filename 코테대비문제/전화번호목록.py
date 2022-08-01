from itertools import combinations
def solution(phone_book):   # 효율성 0/4
    if len(phone_book) == 1:
        return True
    else:
        answer = True
        for nums in list(combinations(phone_book, 2)):
            if nums[0].startswith(nums[1]) or nums[1].startswith(nums[0]):
                answer= False
                break
        return answer


def solution2(phone_book):    # 효율성 2/4
    phone_book.sort(key=len)
    while len(phone_book) > 1:
        num = phone_book.pop(0)
        for n in phone_book:
            if n.startswith(num):
                return False
    return True

def solution3(phone_book):    # 효율성 4/4
    answer = True
    
    phone_book.sort() # 접두어라면 숫자에 따라 sort했을 때 바로 다음에 나옴!
    
    for i in range(len(phone_book)-1):
        # 현재 숫자랑 다음 숫자의 현재숫자 글자만큼이 같은지 확인
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer