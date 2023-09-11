def solution(s):
    idx_dict={}
    answer = []
    for i, chr in enumerate(s):
        if chr not in idx_dict.keys():
            answer.append(-1)
            idx_dict[chr]=[i]
        else:
            answer.append(i-idx_dict[chr][-1])
            idx_dict[chr].append(i)
            
    return answer

# -1을 나올때마다 추가하지 않고, 먼저 -1로 된 리스트 만들어두고 시작

def solution(s):
  answer=[-1]*len(s)
  idx_dict={}
  for idx, chr in eumerate(s):
    if chr in idx_dict:
      answer[idx]=idx-idx_dict[chr]
    idx_dict[chr]=idx
  return answer
