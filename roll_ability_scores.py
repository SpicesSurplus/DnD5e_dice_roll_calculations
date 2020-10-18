import die_maker

def main():
    die1 = die_maker.Die()
    print("\nThis program rolls ability scores!")
    print("______________________________________________________")
    score_names = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    for i in range(6):
        print("\n"+ str(score_names[i]))
        rolls = roll_four_times(die1)
        print("\nThese numbers were rolled: ",str(rolls))
        find_top_three_and_add(rolls)
        print("______________________________________________________")


def roll_four_times(die1):
    roll1 = die1.roll()
    roll2 = die1.roll()
    roll3 = die1.roll()
    roll4 = die1.roll()

    #print(roll1)
    #print(roll2)
    #print(roll3)
    #print(roll4)

    rolls = []

    rolls.append(roll1)
    rolls.append(roll2)
    rolls.append(roll3)
    rolls.append(roll4)


    return rolls

def find_top_three_and_add(rolls):
    #print("\nHere is what we rolled: "+ str(rolls))

    min_value = min(rolls)
    #print("\nThis is our smallest value: "+ str(minval))
    #print("\nThis won't be included in our score")
    rolls[rolls.index(min_value)] = 0  
    ability = sum(rolls)

    print("\nAbility score: "+str(ability))

#call main function here
main()
