print('請輸入兩個正整數,第一個數不能大於第二個數')
num1 = int( input('請輸入第一個正整數： ') )
num2 = int( input('請輸入第二個正整數： ') )

if num1 > num2 :
    print('請輸入正確條件之正整數！')
count = 0
result = 0
for num3 in range(num1,num2+1):
    if num3 % 7 == 0 or num3 % 11 == 0:
        print("{:<4}".format(num3),end='')
        count += 1
        result = result + num3
        if count % 10 == 0:
            print()
print('\n7與11的倍數總共有{}個'.format(count))
print('7與11的倍數總和為:{}'.format(result))