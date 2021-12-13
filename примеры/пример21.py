class user1():
    def __init__(self):
        self.NA = []
        name = input('введите имя первого пользователя --> ')
        age = int(input("введите его возраст --> "))
        self.age_name(name, age)
    def print_all(self):
        print(self.NA)

    def age_name(self, name, age):
        self.NA.append(name)
        self.NA.append(age)

if __name__ =="__main__":
    # создание экземпляра класса
    usr = user1()
    # использование функции класса
    usr.print_all()
