def solution(my_str, n):
    answer = []
    start=0
    end=0
    while True:
        end+=n
        if end>=len(my_str):
            answer.append(my_str[start:])
            break
        answer.append(my_str[start:end])
        start+=n

    return answer

# 굳이 start, end 둘 다 쓸 필요 없음
# 인덱싱의 끝나는 부분은 자료의 길이 초과해도 상관없음

def solution(my_str, n):
    answer=[]
    idx=0
    while idx<len(my_str):
        answer.append(my_str[idx:idx+n])
    return answer

# list comprehension 사용

def solution(my_str,n):
    return [my_str[idx:idx+n] for idx in range(0,len(my_str),n)]
