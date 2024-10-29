def solution(age):
    alphabet = "abcdefghij"
    
    answer = ''.join(alphabet[int(digit)] for digit in str(age))
    return answer

