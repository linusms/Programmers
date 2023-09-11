from collections import defaultdict

def solution(survey, choices):
    answer_dict=defaultdict(int)
    for q, ans in zip(survey, choices):
        if ans in [5,6,7]:
            answer_dict[q[1]]+=ans-4
        elif ans in [1,2,3]:
            answer_dict[q[0]]+=4-ans
    
    answer=""
    for psn1, psn2 in ["RT", "CF", "JM", "AN"]:
        answer+=psn1 if answer_dict[psn1]>=answer_dict[psn2] else psn2
    
    return answer
