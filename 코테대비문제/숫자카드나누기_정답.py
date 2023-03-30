from math import gcd
# 리스트의 최대공약수 찾는 함수
def getGCD(arr):
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd(g, arr[i])
    return g

def check(arr1, arr2):  # arr1의 최대공약수가 arr2를 다 나눌 수 없는지 확인
    g = getGCD(arr1)
    if 0 not in [i%g for i in arr2] and g != 1:
        return g
    else:
        return 0

def solution(arrayA, arrayB):
    answer = 0
    g1 = check(arrayA, arrayB)
    g2 = check(arrayB, arrayA)
    return max(g1, g2)


###### 최대공약수 math 라이브러리 사용 x
# def GCD(a, b):
#     for i in range(min(a, b), 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i