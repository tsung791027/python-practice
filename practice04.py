def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)
    
a,b = input('請輸入兩個數字,中間以逗點做分隔： ').split(',')
a = int(a)
b = int(b)

print(a,'與',b,'的最大公因數為',gcd(a,b))


def primeTest(num1):
    if num1 <= -1 or num1 == 1:
        return False
    else:
        for i in range(2,num1):
            if num1 % i ==0 :
                return False
        return True
                
while True:     
    n = int(input('請輸入整數： '))
    if n == -9999:
        print('程式結束')
        break
    if primeTest(n):
        print(n,'為質數')
    else:
        print(n,'為非質數')
