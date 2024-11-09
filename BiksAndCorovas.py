import random
import os
class BiksAndCorovas():
    def __init__(self, login=''):
        if login=='':
            self.login=input("Who are you, warrior?\n")
        else: self.login=login
        self.number_of_digits=int(input("How many IQ do you think you have?\n"))
        self.number_of_steps=0
        while self.number_of_digits>9 or self.number_of_digits<1:
            print("Error: The IQ level must be between 1 and 9.")
            self.number_of_digits=int(input("Please try again.\n"))
        self.word=self.generate_word(self.number_of_digits)
        self.time=0.1
    
    def save_result(self):
        if not os.path.exists('statistics'):
            os.mkdir('statistics')
        if not os.path.exists('statistics/'+self.login):
            os.mkdir('statistics/' + self.login)
        with open('statistics/' + self.login + '/' + str(self.number_of_digits) + '.txt', 'a') as file:
            file.write(f'{self.number_of_steps} / {self.word} / {self.time}\n')

    def generate_word(self, number_of_digits):
        word=''
        for i in range(number_of_digits):
            digit = random.randint(0,9)
            while str(digit) in word:
                digit = random.randint(0,9)
            word+=str(digit)
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
            if not (i in ['0','1','2','3','4','5','6','7','8','9']):
                print("Error: The guess must only contain digits.")
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

