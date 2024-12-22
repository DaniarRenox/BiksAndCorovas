import random
import os
class BiksAndCorovas():
    def __init__(self, login='', word_length=0, number_of_letters=0):

        if login=='':
            self.login=input("Who are you, warrior?\n")
        else: self.login=login
        self.word_length = word_length
        self.number_of_letters = number_of_letters
        self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'[:self.number_of_letters:]

        if login=='' or input("Do you want to pick previous settings? y/n\n")=='n':
            self.number_of_letters=int(input("How many letters are in the alphabet?\n"))
            self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'[:self.number_of_letters:]

            self.word_length=int(input("How many IQ do you think you have?\n"))
            while self.word_length>35 or self.word_length<1:
                print("Error: The IQ level must be between 1 and 35.")
                self.word_length=int(input("Please try again.\n"))
        
        print(f'Ok then the last letter of the alphabet is {self.alphabet[-1]} and word_length is {self.word_length}')

        self.number_of_steps=0
        
        self.word=self.generate_word(self.word_length)
        self.time=0.1

    def save_result(self):
        if not os.path.exists('statistics'):
            os.mkdir('statistics')
        if not os.path.exists('statistics/'+self.login):
            os.mkdir('statistics/' + self.login)
        with open('statistics/' + self.login + '/' + str(self.word_length) + '_' + str(self.number_of_letters) + '.txt', 'a') as file:
            file.write(f'{self.number_of_steps} / {self.word} / {self.time}\n')

    def show_statistics(self):
        with open('statistics/'+ self.login + '/' + str(self.word_length) + '_' + str(self.number_of_letters) + '.txt', 'r') as file:
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
                    hardest_word=string[word_space+3:word_space+3+self.word_length:]
                    hardest_word_time=time_taken
                if number_of_guesses<easiest_word_guesses:
                    easiest_word_guesses=number_of_guesses
                    easiest_word=string[word_space+3:word_space+3+self.word_length:]
                    easiest_word_time=time_taken
                
                if time_taken>longest_time:
                    longest_time=time_taken
                    longest_time_word=string[word_space+3:word_space+3+self.word_length:]
                    longest_time_word_guesses=number_of_guesses
                if time_taken<shortest_time:
                    shortest_time=time_taken
                    shortest_time_word=string[word_space+3:word_space+3+self.word_length:]
                    shortest_time_word_guesses=number_of_guesses

                sum += number_of_guesses

        middle_result=sum/len(strings)
        
        print(f'Amount of attempts is {len(strings)}\nThe middle result is {middle_result}'
            f'\nThe hardest word ever is {hardest_word} with {hardest_word_guesses} guesses in {hardest_word_time} seconds'
            f'\nThe easiest word ever is {easiest_word} with {easiest_word_guesses} guesses in {easiest_word_time} seconds'
            f'\nThe longest time taken is {longest_time} seconds for the word {longest_time_word} in {longest_time_word_guesses} guesses'
            f'\nThe shortest time taken is {shortest_time} seconds for the word {shortest_time_word} in {shortest_time_word_guesses} guesses')

    def generate_word(self, word_length):
        word=''
        local_alphabet=self.alphabet
        for i in range(word_length):
            letter = random.choice(local_alphabet)
            local_alphabet=local_alphabet.replace(letter, '')
            word+=letter
        return word

    def fool_protection(self, user_guess):
        if user_guess=='im dumb':
            print(f"ok u lil cheater -__- here is the number i guessed: {self.word}")
            print("////////////////////////////////////////////////////////////////////")
            return True
        if len(user_guess)!=len(self.word):
            print("Error: The guess must be the same length as the word.")
            return True
        for i in user_guess:
            if not (i in self.alphabet):
                print(f"Error: The guess can contain digits and letters till the letter {self.alphabet[-1]} (including).")
                return True
        return False

    def guess_word(self):
        self.number_of_steps+=1
        user_guess=input("Ok show me you IQ lvl: \n")
        while self.fool_protection(user_guess):
            user_guess=input('cringe but ok, try again...\n')

        biks=0
        corovas=0
        for i in range(len(self.word)):
            if self.word[i]==user_guess[i]:
                biks+=1
            elif user_guess[i] in self.word:
                corovas+=1

        if user_guess==self.word:
            print("Congratulations! You guessed the word correctly.\n")
            return True
        else:
            print("You didn't get it right, but here are your tips:\n" + "Number of biks: " + str(biks) + "\nNumber of corovas: " + str(corovas) + '\n')
            return False

