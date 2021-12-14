#  создание функции
def hello():
    print('Hello, World!')
#  вызов функции
hello()

# функция с параметром
def user_hello(name):
    print('hello, ', name)
user_hello('Paul')

# можно передать несколько параметров
def summ(stop, s, u, x):
    for i in range(stop):
        s += u
        u += x
    # функция возвращает переменную
    return s
# присваиваем переменной то, что вернула функция
s = summ(23, 10, 14, 4)
print(s)

usr = []
def user(name, age):
    global usr
    usr.append(name)
    usr.append(age)

def print_user():
    print(usr)
user('Rodion', '15')
print_user()
