def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    numbers = [str(num) for num in numbers]
    numbers.sort(key = lambda x: x*3, reverse=True)
    return ''.join(numbers)