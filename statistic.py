from biks_and_corovas import Game
import os

class Statistic():

    def __init__(self):
        pass

    def save_result(self, game : Game):
        print(f'you did it in {game.number_of_steps} steps, and it took {game.time} seconds. Do you want to save your result? y/n')
        if input()=='y':
            if not os.path.exists('statistics'):
                os.mkdir('statistics')
            if not os.path.exists('statistics/'+game.login):
                os.mkdir('statistics/' + game.login)
            with open('statistics/' + game.login + '/' + str(len(game.alphabet)) + '_' + str(game.number_of_letters) + '.txt', 'a') as file:
                file.write(f'{game.number_of_steps} / {game.word} / {game.time}\n')
        print('----------------------------------------------------------------')

    def show_stats(self, login):
        print("Available statistics:")
        files = [f[:f.find(".txt"):] for f in os.listdir(f"./statistics/{login}")]
        for file in files:
            print(file)
        print ('What statistics would you like to see? Type in alphabet length, then type number of letters in the word')
        alphabet_length=int(input())
        number_of_letters=int(input())
        print('----------------------------------------------------------------')
        try:
            with open('statistics/'+ login + '/' + str(alphabet_length) + '_' + str(number_of_letters) + '.txt', 'r') as file:
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

                    if number_of_guesses>=hardest_word_guesses:
                        hardest_word_guesses=number_of_guesses
                        hardest_word=string[word_space+3:word_space+3+number_of_letters:]
                        hardest_word_time=time_taken
                    if number_of_guesses<easiest_word_guesses:
                        easiest_word_guesses=number_of_guesses
                        easiest_word=string[word_space+3:word_space+3+number_of_letters:]
                        easiest_word_time=time_taken
                    
                    if time_taken>longest_time:
                        longest_time=time_taken
                        longest_time_word=string[word_space+3:word_space+3+number_of_letters:]
                        longest_time_word_guesses=number_of_guesses
                    if time_taken<shortest_time:
                        shortest_time=time_taken
                        shortest_time_word=string[word_space+3:word_space+3+number_of_letters:]
                        shortest_time_word_guesses=number_of_guesses

                    sum += number_of_guesses

            middle_result=sum/len(strings)
            print(f'Alphabet length is {alphabet_length}, word length is {number_of_letters}'
                f'\nAmount of attempts is {len(strings)}\nThe average amount of guesses is {middle_result}'
                f'\nThe hardest word ever is {hardest_word} with {hardest_word_guesses} guesses in {hardest_word_time} seconds'
                f'\nThe easiest word ever is {easiest_word} with {easiest_word_guesses} guesses in {easiest_word_time} seconds'
                f'\nThe longest time taken is {longest_time} seconds for the word {longest_time_word} in {longest_time_word_guesses} guesses'
                f'\nThe shortest time taken is {shortest_time} seconds for the word {shortest_time_word} in {shortest_time_word_guesses} guesses')
            print('----------------------------------------------------------------')
        except:
            print(f"There is no records on these parametres: \nAlphabet length: {alphabet_length}\nNumber of letters: {number_of_letters}")