# 드래그 끝 좌표는 구한 점 위치에 +1을 해줘야 한다.
# 이런 디테일을 놓치면 실전에서 틀리게 된다

def solution(wallpaper):
    y_exist=[]
    x_start, x_end=len(wallpaper [0]),0
    for i, row in enumerate(wallpaper):
        if row.find("#")!=-1:
            x_start=min(row.find("#"), x_start) 
            x_end=max(row.rfind("#"), x_end) 
            y_exist.append(i)
    
    y_start,y_end=min (y_exist), max(y_exist)
    
    return [y_start, x_start, y_end+1, x_end+1]

# 같은 원리인데 .find 보다 이중 반복문이 더 빠른건지 잘 모르겠음

def solution(wallpaper):
  x,y=[],[]
  for i in range(len(wallpaper)):
    for j in range(len(wallpaper[i]):
      if wall[i][j]=="#":
        x.append(i)
        y.append(j)
  return [min(x), min(y), max(x)+1 ,max(y)+1]
