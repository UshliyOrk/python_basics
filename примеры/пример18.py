list1 = []
for i in range(10):  # конечное число 9
    list1.append("Python " + str(i))


list2 = []
for t in range(3,6):  # от 3 до 5
    list2.append("World " + str(t))


for s in range(2, 123, 4):  # от 2 до 122 с шагом 4
    print(str(s) +" =", float(s))


for r in list1:  # r поочерёдно принимает все значения list1
    print(r)

for i in range(2, 5):
    print(i)
else:
    print('цикл успешнозавершен')

for i in range(2, 5):
    print(i)
    break
else:
    print('цикл успешнозавершен')
print('цикл прерван')

a = True
b = False
x = 0
while a and not b:
    x += 1
    if x == 3:
        a = False