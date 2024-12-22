from BiksAndCorovas import BiksAndCorovas
import time
#main func
def main(login='', word_length=0, number_of_letters=0):
    game=BiksAndCorovas(login, word_length, number_of_letters)
    start_time=time.time()
    while not game.guess_word():
        pass
    game.time=round(time.time() - start_time,2)
    print(f'you did it in {game.number_of_steps} steps, and it took {game.time} seconds. Do you want to save your result? y/n')
    if input()=='y':
        game.save_result()
    print ('do you want to show your stats on this IQ level? y/n')

    if input()=='y':
        game.show_statistics()        
    print('----------------------------------------------------------------')
    print('Wanna play again? y/n')

    if input()=='y':
        main(game.login, game.word_length, game.number_of_letters)

main()