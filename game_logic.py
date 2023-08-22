import random
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
starting_money = int(config['DEFAULT']['MY_MONEY'])


def play_game():
    money = starting_money
    numbers = list(range(1, 31))

    while True:
        print("Ваши деньги: $", money)

        bet = int(input("Выберите число от 1 до 30: "))
        if bet not in numbers:
            print("Неправильный выбор числа!")
            continue

        amount = int(input("Сделайте ставку: "))
        if amount > money:
            print("У вас недостаточно средств для сделки ставки!")
            continue

        winning_number = random.choice(numbers)

        if bet == winning_number:
            money += amount * 2
            print("Вы победили и получаете удвоенную сумму!")
        else:
            money -= amount
            print("Вы проиграли!")

        play_again = input("Хотите сыграть еще? (да/нет): ")
        if play_again.lower() != "да":
            break

    print("Ваш итоговый капитал: $", money)