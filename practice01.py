#撰寫一個程式，讓使用者輸入兩個整數a,b
#接著輸入其中一個運算子，最後輸出兩個整數運算結果
int1 = int(input("請輸入第一個整數： "))
int2 = int(input("請輸入第二個整數： "))
fn1 = input("請輸入想使用的運算子： ")


if fn1 == '+':
    print(int1 + int2)
elif fn1 == '-':
    print(int1 - int2)
elif fn1 == '*':
    print(int1 * int2)
elif fn1 == '/':
    if int2 == 0:
        print('除數不可為0!!')
    else:
        print(int1 / int2)
elif fn1 == '//':
    if int2 == 0:
        print('除數不可為0!!')
    else:
        print(int1 // int2)
elif fn1 == '%':
    if int2 == 0:
        print('除數不可為0!!')
    else:
        print(int1 % int2)
elif fn1 == '**':
    print(int1 ** int2)
else:
    print('請輸入有效之運算子')
    
#練習2 
#撰寫程式,讓使用者輸入一個西元年年份,程式輸出
#顯示是否為閏年
    
year = int(input('請輸入一個西元年份：'))    
    
if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
    print(year,'年是閏年')
else:
    print(year,'年不是閏年')
    
#range()練習
#撰寫程式,讓使用者輸入一個數字n,則用@字元列印出n層的反三角形

n = int(input('請輸入一個數字: '))

for i in range(n,0,-1):
    print('@'* i)
