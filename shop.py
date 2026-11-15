import sys

print("Добро пожаловать в интернет-магазин 'Тыдыщ!'")
polzovateli = {"Masha": 1234, "Sasha": 4321}
tovari = {"Бургер": 100, "Бабушкина квартира(покупайте быстрее, пока она не знает)": 100000000000, "Карандаш": 99999999999999999999999999}
c = 0
a = input("У вас уже есть аккаунт?(да/нет) ").lower()
if a == "да" and c == 0:
    d = [2, 1, 0]
    for i in range(3):
        name = input("Введите логин ")
        password = input("Введите пароль ")
        try:
            if polzovateli[name] == password:
                print(f"Успешный вход, {name}!")
                c = 1
                break
            
        except:
            if d[i] == 0:
                print("Повторите попытку позже")
                sys.exit()
            else:
                print(f"Неверный пароль, осталось попыток: {d[i]}")

if a == "нет" and c == 0:
    name = input("Введите логин ")
    password = input("Введите пароль ")
    polzovateli[name] = password
    print("Аккаунт успешно создан! Приятного пользования!")

bal = int(input("Какой у вас балланс?"))
rub = input("Какая у вас валюта?(1.Рубли 2.Доллары 3.Евро)").lower()

if rub == "1" or rub == "рубли":
    new_bal = bal
    print(f"Ваш баланс в рублях: {new_bal}")
if rub == "2" or rub == "доллары":
    new_bal = bal * 80
    print(f"Ваш баланс в рублях: {new_bal}")
if rub == "3" or rub == "евро":
    new_bal = bal * 90
    print(f"Ваш баланс в рублях: {new_bal}")
else:
    new_bal = bal
    print("Неизвестная валюта")

