def solution(s):
    answer=[]
    for chr in s.split(" "):
        if chr=="Z":
            answer.pop()
            continue
        answer.append(int(chr))
    return sum(answer)
