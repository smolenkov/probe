from game_engine import get_number, check_number, coin_number, game_over


def start_game():
    get_number()
    while True:
        print('Введите ', coin_number, '-х значное число')
        user_number = input()
        cow, bull = check_number(user_number)
        print('коров - ', cow, 'быков - ', bull)

        if game_over():
            break
    print('Поздравляем, вы выиграли !')
    print('Хотите сыграть еще раз?')
    again = input("Y / N ")
    if again == 'Y' or 'y':
        print('Отлично!')
    start_game()
start_game()