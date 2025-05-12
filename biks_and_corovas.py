import random
import os
class Game():
    def __init__(self, login=''):
        self.set_alphabet()
        self.set_number_of_letters()
        self.login=login
        self.word=self.generate_word(self.number_of_letters)
        self.time : float
        self.number_of_steps=0

    def set_alphabet(self):
        alphabet_length = int(input("How many letters are in the alphabet?\n NOTE: amount of letters has to be between 0 and 37\n  NOTE: set 10 for standart difficulty\n"))
        while alphabet_length<1 or alphabet_length>36:
            print("Error: input value has to be more than 0 and less than 37")
            alphabet_length = int(input("How many letters are in the alphabet?\n NOTE: amount of letters has to be between 0 and 37\n  NOTE: set 10 for standart difficulty\n"))
        self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'[:alphabet_length:]
        print(f'Ok then the last letter of the alphabet is {self.alphabet[-1]}')
        print('----------------------------------------------------------------')

    def set_number_of_letters(self):
        self.number_of_letters=int(input("How many IQ do you think you have?\n NOTE: IQ has to be more than 1 and less than amount of letters in the alphabet\n  NOTE: set 4 for standart difficulty\n"))
        while self.number_of_letters<1 or self.number_of_letters>len(self.alphabet):
            print("Error: The IQ level must be more than 1 and less than amount of letters in the alphabet.\n")
            print("Want to change amount of letters in the alphabet? y/n\n")
            if input()=='y':
                self.alphabet=self.set_alphabet()
            self.number_of_letters=int(input("Input your IQ level again.\n"))
        print('----------------------------------------------------------------')


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
            print('----------------------------------------------------------------')

        biks=0
        corovas=0
        for i in range(len(self.word)):
            if self.word[i]==user_guess[i]:
                biks+=1
            elif user_guess[i] in self.word:
                corovas+=1

        if user_guess==self.word:
            print("Congratulations! You guessed the word correctly.\n")
            print('----------------------------------------------------------------')
            return True
        else:
            print("You didn't get it right, but here are your tips:\n" + "Number of biks: " + str(biks) + "\nNumber of corovas: " + str(corovas) + '\n')
            print('----------------------------------------------------------------')
            return False

