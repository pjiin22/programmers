def solution(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return 1  # n이 제곱수인 경우
        i += 1
    return 2  # n이 제곱수가 아닌 경우
