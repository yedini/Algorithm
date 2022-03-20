# input 받아서 원소 하나씩 떼서 list로
l = list(input())

letters = []
nums = 0
for i in l:
    if str.isdigit(i) == True:  # 숫자일 경우 더하기
        nums += int(i)
    else:                       # 문자일 경우 letters 리스트에 추가
        letters.append(i)

# 정렬한 letters와 숫자합을 다 이어붙여서 출력
# 숫자가 0인 경우도 고려해야함!!
if nums == 0:
    print(''.join(sorted(letters)))
else:
    print(''.join(sorted(letters))+str(nums))