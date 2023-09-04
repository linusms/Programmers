def solution(chicken):
    answer=0
    service=0
    while chicken>=10:
        service=chicken//10
        chicken=chicken%10
        chicken=service+chicken
        answer+=service
    return answer
