from BiksAndCorovas import BiksAndCorovas
import time
#main func
def main(login=''):
    game=BiksAndCorovas(login)
    start_time=time.time()
    while not game.guess_word():
        pass
    game.time=round(time.time() - start_time,2)
    print(f'you did it in {game.number_of_steps} steps, and it took {game.time} seconds. Do you want to save your result? y/n')
    if input()=='y':
        game.save_result()
    print ('do you want to show your stats on this IQ level? y/n')

    if input()=='y':
        with open('statistics/'+ game.login + '/' + str(game.number_of_digits) + '.txt', 'r') as file:
            strings = file.readlines()

            sum = 0
            hardest_word=''
            hardest_word_guesses=0
            hardest_word_time = 0.1

            
            
            easiest_word=''
            easiest_word_guesses=10000
            easiest_word_time=10000000

            shortest_time=10000000
            shortest_time_word=''
            shortest_time_word_guesses=1
            longest_time=0.1
            longest_time_word=''
            longest_time_word_guesses=1

            for i in range(len(strings)):
                
                string=strings[i].strip()
                number_of_guesses=int(string[:string.find(' '):])
                word_space=string.find(' ')
                time_space=string.find(' ', word_space+3)
                time_taken=float(string[time_space+3:])

                if number_of_guesses>hardest_word_guesses:
                    hardest_word_guesses=number_of_guesses
                    hardest_word=string[word_space+3:word_space+3+game.number_of_digits:]
                    hardest_word_time=time_taken
                if number_of_guesses<easiest_word_guesses:
                    easiest_word_guesses=number_of_guesses
                    easiest_word=string[word_space+3:word_space+3+game.number_of_digits:]
                    easiest_word_time=time_taken
                
                if time_taken>longest_time:
                    longest_time=time_taken
                    longest_time_word=string[word_space+3:word_space+3+game.number_of_digits:]
                    longest_time_word_guesses=number_of_guesses
                if time_taken<shortest_time:
                    shortest_time=time_taken
                    shortest_time_word=string[word_space+3:word_space+3+game.number_of_digits:]
                    shortest_time_word_guesses=number_of_guesses

                sum += number_of_guesses

        middle_result=sum/len(strings)
        
        print(f'Amount of attempts is {len(strings)}\nThe middle result is {middle_result}'
            f'\nThe hardest word ever is {hardest_word} with {hardest_word_guesses} guesses in {hardest_word_time} seconds'
            f'\nThe easiest word ever is {easiest_word} with {easiest_word_guesses} guesses in {easiest_word_time} seconds'
            f'\nThe longest time taken is {longest_time} seconds for the word {longest_time_word} in {longest_time_word_guesses} guesses'
            f'\nThe shortest time taken is {shortest_time} seconds for the word {shortest_time_word} in {shortest_time_word_guesses} guesses')
        
    print('----------------------------------------------------------------')
    print('Wanna play again? y/n')

    if input()=='y':
        main(game.login)

main()