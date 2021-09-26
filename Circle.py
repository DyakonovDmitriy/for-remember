# i=None
# while i!="Volvo":
#     i=input('введите марку автомобиля \n')
#     if i=='Volvo': break
#     print('неверно')
# print('верно')

for i in range(10):
    if i==7: break
    if i<=3: continue
    print(i)

a=input('anything')
b=input('anything')
print(a,id(a))
print(b,id(b))
id(a)=id(b)
print(a)

