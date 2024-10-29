def solution(my_string):
    # 문자열을 소문자로 변환하고 정렬
    result = ''.join(sorted(my_string.lower()))
    return result
