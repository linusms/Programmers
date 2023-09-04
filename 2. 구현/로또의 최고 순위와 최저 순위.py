def solution(lottos, win_nums):
    answer = []
    match=0
    zeros=0
    for num in lottos:
        if num in win_nums:
            match+=1
        elif num==0:
            zeros+=1
        
    lowest=7-match
    highest=lowest-zeros
    if lowest==7:
        lowest=6
        highest=6
        if zeros!=0:
            highest=lowest-zeros+1
    answer=[highest, lowest]
    return answer
