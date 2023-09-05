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

# 앞선 코드는 for 문 + .count() 함수로 시간복잡도 n^2
# Counter 함수 사용해 시간복잡도를 줄인다

from collections import Counter

def solution(participant, completion):
    complete_runner=Counter(completion)
    
    for name in participant:
        if name in complete_runner and complete_runner[name]>0:
            complete_runner[name]-=1
        else:
            return name


# Counter 의 성질 이용

from collection import Counter

def solution(participant, completion):
    participants=Counter(participant)
    completes=Counter(completion)

    # Counter는 +,-가 가능하고, value가 큰 순서대로 정렬되기 때문
    return list(participants-completes)[0]


