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
