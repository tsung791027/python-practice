dict1 = dict()
print('請輸入第1個字典： ')
while True:
    key = input('key: ')
    if key =='end':
        break
    value = input('Value: ')
    dict1[key] = value
dict2 = dict()
print('請輸入第2個字典： ')
while True:
    key = input('key: ')
    if key =='end':
        break
    value = input('Value: ')
    dict2[key] = value

dict1.update( dict2 )

for i in sorted(dict1.keys()):
    print(i,': ',dict1[i],sep='')