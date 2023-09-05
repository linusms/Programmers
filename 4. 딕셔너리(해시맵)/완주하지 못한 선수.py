# 결과는 잘 나오지만, 효율성 테스트에서 아웃

def solution(participant, completion):
    runner={}
    runner_finish=defaultdict(int)
    for name in participant:
        runner[name]=participant.count(name)
    for name in runner:
        runner_finish[name]=completion.count(name)
        if runner_finish[name]!=runner[name]:
            answer=name
            break
        
    return answer
