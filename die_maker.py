import random

#The Die class simulates a die that can be rolled
#This includes methods for all seven kinds of main dice(D4, D6, D8, D10, D12, D20, percentile dice)

class Die:

    #init__ method initializes the die
    def __init__(self):
        #values set to 0 initially
        #self.__sides = int(input("How many sides does the die have? ")) max number of sides
        self.__sides = 0
        self.__num = 0 #number on a particular side

    def get_sides(self):
        return self.__sides

#roll 20 sided dice
    def roll_twenty(self):
        self.__sides = 20
        self.__num = random.randint(1,20)

        return self.__num #returns whatever a player rolled

#roll 6 sided dice
    def roll_six(self):
        self.__sides = 6
        self.__num = random.randint(1,6)

        return self.__num

#roll 4 sided dice (pick random number one out three on one side!)
#I'm going to implement this
#it will happen


#roll 8 sided dice
    def roll_eight(self):
        self.__sides = 8
        self.__num = random.randint(1,8)
        return self.__num

#roll 10 sided dice
    def roll_ten(self):
       self.__sides = 10
       self.__num = random.randint(1,10)
       return self.__num

#roll 12 sided dice
    def roll_twelve(self):
        self.__sides = 12
        self.__num = random.randint(1,12)
        return self.__num


#roll percentile die
#This will also happen sometime
#ah


#die1 = Die()


