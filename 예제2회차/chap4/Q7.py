# string으로 받아서 list화:숫자 하나씩 담은 리스트로 => map으로 int 변환 => list화
nums = list(map(int, list(input())))

# 중간위치: 그냥 / 하면 float로 반환 => // 를 써서 정수로 만들기
med = len(nums)//2

if sum(nums[:med]) == sum(nums[med:]):
    print("LUCKY")
else:
    print("READY")