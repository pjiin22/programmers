def solution(numbers):
    # 배열을 정렬
    numbers.sort()
    # 가장 큰 두 수의 곱과 가장 작은 두 수의 곱 중 최댓값을 선택
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
