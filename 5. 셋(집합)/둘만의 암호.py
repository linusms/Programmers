#런타임 에러 발생

import string

def solution(s, skip, index):
    alp_list=sorted(list(set(string.ascii_lowercase)-set(skip)))
    answer = ''
    for chr in s:
        chr_idx=alp_list.index(chr)+index
        if chr_idx<=len(alp_list)-1:
            answer+=alp_list[chr_idx]
        else:
            answer+=alp_list[chr_idx-len(alp_list)]
    return answer

# 에러없는 버전.  alp_list의 길이가 바뀌는데
# 길이를 초과하는 인덱스의 경우 처리에서 %(나머지)로 처리하는게 더 깔끔
# 위의 else: 부터 문제가 있어보임.

import string

def solution(s, skip, index):
    alp_list=sorted(set(string.ascii_lowercase)-set(skip))
    answer = ''
    for chr in s:
        chr_idx=alp_list.index(chr)+index
        answer+=alp_list[chr_idx%(len(alp_list))]
    return answer

# 딕셔너리에 인덱스 위치 저장하고 불러와서 인덱스 구하는 방법
# 아마도 .index() 보다 빠를 것 같다.

import string

def solution(s, skip, index):
    alp_list=sorted(set(string.ascii_lowercase)-set(skip))
    answer = ''
    for chr in s:
        idx_dict={chr:idx for idx, chr in enumerate(alp_dict))
        answer+=alp_list[chr_idx%(len(alp_list))]
    return answer
