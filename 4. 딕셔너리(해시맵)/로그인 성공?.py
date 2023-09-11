def solution(id_pw, db):
    db_dict={}
    for key, value in db:
        db_dict[key]=value
    
    if id_pw[0] not in db_dict.keys():
        answer="fail"
    elif db_dict[id_pw[0]]!=id_pw[1]:
        answer="wrong pw"
    else:
        answer = "login"
        
    return answer

# 리스트를 바로 딕셔너리로 바꾸는 방법 
# [[key,value]],...]로 구성된 리스트를 딕셔너리로 변환(dict)

def solution(id_pw, db):
  val=dict(db).get(id_pw[0])
  if val:
    if val==id_pw[1]:
      return "login"
    return "wrong pw"
  return "fail"
