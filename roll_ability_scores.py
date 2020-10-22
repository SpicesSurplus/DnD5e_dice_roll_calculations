import die_maker

def main():
    die1 = die_maker.Die()
    print("\nThis program rolls ability scores!")
    print("______________________________________________________")
    score_names = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    modifier = 0

    #prints what numbers were rolled for each score
    for i in range(6):
        print("\n"+ str(score_names[i]))
        rolls = roll_four_times(die1)
        print("\nThese numbers were rolled: ",str(rolls))

        #prints ability score
        ability_score = find_top_three_and_add(rolls)
        print("\nAbility score: " + str(ability_score))

        #prints modifier
        modifier = calc_modifier(ability_score)
        print("\nModifier: " + str(modifier))




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

    return ability

def calc_modifier(ability_score):
    if (ability_score == 1):
        modifier = -5
    elif (ability_score == 2 or ability_score == 3):
        modifier = -4
    elif (ability_score == 4 or ability_score == 5):
        modifier = -3
    elif (ability_score == 6 or ability_score == 7):
        modifier = -2
    elif (ability_score == 8 or ability_score == 9):
        modifier = 1
    elif (ability_score == 10 or ability_score == 11):
        modifier = 0
    elif (ability_score == 12 or ability_score == 13):
        modifier = 1
    elif (ability_score == 14 or ability_score == 15):
        modifier = 2
    elif (ability_score == 16 or ability_score == 17):
        modifier = 3
    elif (ability_score == 18 or ability_score == 19):
        modifier = 4
    elif (ability_score == 20 or ability_score == 21):
        modifier = 5
    elif (ability_score == 22 or ability_score == 23):
        modifier = 6
    elif (ability_score == 24 or ability_score == 25):
        modifier = 7
    elif (ability_score == 26 or ability_score == 27):
        modifier = 8
    elif (ability_score == 28 or ability_score == 29):
        modifier = 9
    elif (ability_score == 30):
        modifier = 10

    return modifier

#call main function here
main()
