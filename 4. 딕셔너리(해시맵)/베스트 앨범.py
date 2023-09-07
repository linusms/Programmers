# 막혔던 부분

from collections import defaultdict

def solution(genres, plays):
    s_dict=defaultdict(list)
    genre_dict=defaultdict(int)
  
# 1. 튜플로 된 값을 한번에 여러 개 변수로 받으려면 (a,b)=(1,2) 같이 괄호 필요
    for i, (genre, play) in enumerate(zip(genres, plays)):
        s_dict[genre].append((play,i))
        genre_dict[genre]+=play
      
# 2. 튜플로 된 딕셔너리 idx번째 튜플 원소 기준으로 정렬법: Sorted(dict.items(), key=lambda x: x[idx])
# 내림차순으로 정렬해야 하면  x 앞에 -
    by_plays=sorted(genre_dict.items(), key=lambda x: -x[1])
    
    answer=[]
    
    for genre, play in by_plays:
# 3. 리스트 슬라이싱 시 끝 인덱스는 범위를 넘어도 상관없다
        best_list=sorted(s_dict[genre], key=lambda x: -x[0])[:2]
        answer.extend([idx for play, idx in best_list])
            
    return answer
