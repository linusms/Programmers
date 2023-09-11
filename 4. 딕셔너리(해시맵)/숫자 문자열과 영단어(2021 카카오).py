def solution(s):
    number_eng={'zero':'0', 'one':'1', 'two':'2', 'three':'3', 
                'four':'4', 'five':'5', 'six':'6', 'seven':'7', 
                'eight':'8', 'nine':'9'}
    for eng, num in number_eng.items():
        s=s.replace(eng, num)
        
    answer=int(s)
    
    return answer

# 더 빠르고, 범용적인 풀이

def solution(s):
  number_eng={'zero':'0', 'one':'1', 'two':'2', 'three':'3', 
                'four':'4', 'five':'5', 'six':'6', 'seven':'7', 
                'eight':'8', 'nine':'9'}
  answer=""
  engnum=""
  for chr in s:
    if chr.isnumeric():
      answer+=chr
    else:
      if engnum>2 and engnum in number_eng:
        answer+=number_eng[engnum]
        engnum=""
  return int(answer)
