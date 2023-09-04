def solution(answers):
    supo_array=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    answer =[]
    for supo in supo_array:
            supo_array_idx=0
            test_idx=0
            supo_cnt=0
            while True:
                if supo[supo_array_idx]==answers[test_idx]: supo_cnt+=1
                if supo_array_idx==len(supo)-1: supo_array_idx=-1
                supo_array_idx+=1
                test_idx+=1
                if test_idx==len(answers): 
                    answer.append(supo_cnt) 
                    break

  # 마지막에 정답 횟수가 가장 많은 사람의 번호 찾아내기와, 
  # 동차일때 오름차순 정렬 하는 방법 생각이 어려웠음 
    return [idx+1 for idx, score in enumerate(answer) if score==max(answer)]

# 다른 풀이: 인덱스를 하나씩 더해가고, 특정 값이 되면 초기화하는 과정 필요없이
# 나머지 구하는 함수로 간단히 해결
def solution(answers):
    supo_array=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    scores=[0,0,0]
    for type_idx, ans_type in enumerate(supo_array):
        for idx, ans in enumerate(answers):
            if ans==ans_type[idx%len(ans_type)]:
                scores[type_idx]+=1
            
        
    return [idx+1 for idx, score in enumerate(scores) if score==max(scores)]
