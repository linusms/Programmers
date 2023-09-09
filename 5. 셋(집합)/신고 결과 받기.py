# 오류는 없지만 코드 길이 줄여볼 수 있을 것 같다
# 최대 런타임 시간 225ms

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_dict=defaultdict(set)
    report_cnt_dict=defaultdict(int)
    for r in report:
        r_cnt=0
        user, r_user=r.split(" ")
        if r_user not in report_dict[user]:
            report_cnt_dict[r_user]+=1
        report_dict[user].add(r_user)
    for user in id_list:
        cnt=0
        for r_user in report_dict[user]:
            if report_cnt_dict[r_user]>=k:
                cnt+=1
        answer.append(cnt)
    print(report_cnt_dict)
    print(report_dict)
    return answer
