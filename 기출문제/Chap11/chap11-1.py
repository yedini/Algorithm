N = int(input())
nums = list(map(int, input().split()))
nums.sort()

result = 0 #최종 그룹 수
count = 0  #현재 그룹에 속해있는 모험가 수
for n in nums:
    count += 1   # 현재 그룹에 추가
    if count >= n:   # 현재 모험가 수가 현재 확인중인 공포도보다 크거나 같다면
        result += 1  # 한 그룹으로 묶기 완료
        count = 0    # count 초기화, 다음 모험가부터 새 그룹 형성 시작

print(result)