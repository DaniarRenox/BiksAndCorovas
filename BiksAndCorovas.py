import random
import os
class BiksAndCorovas():
    def __init__(self, login=''):



        if login=='':
            self.login=input("Who are you, warrior?\n")
        else: self.login=login
        self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'[:int(input("How many letters are in the alphabet?\n NOTE: amount of letters has to be between 1 and 37\n  NOTE: set 10 for standart difficulty\n")):]
        print(f'Ok then the last letter of the alphabet is {self.alphabet[-1]}')
        self.number_of_letters=int(input("How many IQ do you think you have?\n NOTE: IQ has to be more than 1 and less than amount of letters in the alphabet\n  NOTE: set 4 for standart difficulty\n"))
        self.number_of_steps=0
        while self.number_of_letters<1 or self.number_of_letters>len(self.alphabet):
            print("Error: The IQ level must be more than 1 and less than amount of letters in the alphabet.\n")
            print("Want to change amount of letters in the alphabet? y/n\n")
            if input()=='y':
                self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'[:int(input("How many letters are in the alphabet?\n")):]
                print(f'Ok then the last letter of the alphabet is {self.alphabet[-1]}')
            self.number_of_letters=int(input("Input your IQ level again.\n"))
        self.word=self.generate_word(self.number_of_letters)
        self.time=0.1
    
    def save_result(self):
        if not os.path.exists('statistics'):
            os.mkdir('statistics')
        if not os.path.exists('statistics/'+self.login):
            os.mkdir('statistics/' + self.login)
        with open('statistics/' + self.login + '/' + str(self.number_of_letters) + '.txt', 'a') as file:
            file.write(f'{self.number_of_steps} / {self.word} / {self.time}\n')

    def generate_word(self, number_of_letters):
        word=''
        local_alphabet=self.alphabet
        for i in range(number_of_letters):
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

