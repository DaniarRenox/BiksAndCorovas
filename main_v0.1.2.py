from biks_and_corovas import Game
from statistic import Statistic
import time
#main func

def set_login(login):
        if login=='':
            print('----------------------------------------------------------------')
            login=input("Who are you, warrior?\n")
            return login
            print('----------------------------------------------------------------')
        return login

def main_menu(login=''):
    print('----------------------------------------------------------------')
    print(f"Welcome to the main menu, {login}!")
    user_input=input("Type anything to play or S for statistics\n")
    print('----------------------------------------------------------------')
    if user_input=='S':
        statistic=Statistic()
        statistic.show_stats(login)
        main_menu(login)

def main(login=''):
    login=set_login(login)
    main_menu(login)
    game=Game(login)
    
    start_time=time.time()
    while not game.guess_word():
        pass
    game.time=round(time.time() - start_time,2)

    statistic = Statistic()
    statistic.save_result(game)

    main(login)


main()