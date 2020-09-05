#撰寫程式，第一排列印1~9,中間間隔一空白以此類推完成三角形
for row in range(1,10):
    for col in range(1,row+1):
        print(col, end=' ')
    print()

#承上題印出倒三角形
for row in range(1,10):
    for col in range(1,10-row+1):
        print(col, end=' ')
    print()

#承上題請列印出倒三角形後從每行開頭開始遞減
for row in range(1,10):
    for col in range(row,10):
        print(col, end=' ')
    print()
    
for row in range(1,10):
    for col in range(row,0,-1):
        print(col, end=' ')
    print()