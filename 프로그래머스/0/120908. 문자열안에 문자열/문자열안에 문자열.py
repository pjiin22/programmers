def solution(str1, str2):
    for i in range(len(str1)):
        if str1[i]==str2[0]:
            if str1[i:i+len(str2)] == str2:
                return 1
            
            
            
    return 2