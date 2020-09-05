x1 = eval(input('請輸入Ａ點的x座標： '))
y1 = eval(input('請輸入Ａ點的y座標： '))
x2 = eval(input('請輸入B點的x座標： '))
y2 = eval(input('請輸入B點的y座標： '))

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

print('A點座標為( {},{} )'.format(x1,y1))
print('B點座標為( {},{} )'.format(x2,y2))
print('兩點的距離為:{:.4f} '.format(distance))