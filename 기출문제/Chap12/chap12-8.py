import re

l = input()

letters = re.findall('[A-Z]', l)   # 알파벳만 찾기
letters.sort()                     # 알파벳 정렬
nums = re.findall('[0-9]', l)      # 숫자만 찾기

result = ''
for i in range(len(letters)):
    result = result + letters[i]   # 알파벳 오름차순으로 붙이기

nums = list(map(int, nums))        # 정수화

print(result+str(sum(nums)))       # 정렬된 알파벳에 숫자합 합쳐서 출력