import sys

print("Добро пожаловать в интернет-магазин 'Тыдыщ!'")
polzovateli = {"Masha": 1234, "Sasha": 4321}
c = 0
a = input("У вас уже есть аккаунт?(да/нет) ")
if a == "да".lower() and c == 0:
    d = [2, 1, 0]
    for i in range(2):
        a = input("Введите логин ")
        b = input("Введите пароль ")
        if polzovateli[a] == b:
            print(f"Успешный вход, {a}!")
            c = 1
            break
        elif d[i] == 0:
            print("Повторите попытку позже")
            sys.exit()
        else:
            print(f"Неверный пароль, осталось попыток: {d[i]}")

# if a == "нет" and c == 0:
#     a = input("Введите логин")
#     b = input("Введите пароль")