# Challenge Questions - 28 Aug 2021
# SOURCE: friends / forums / anywhere
# TOPIC: anytopic


'''Q from Raghav - 28AUG2021:
'SNAKE', 'WATER', 'GUN' game (aka rock, paper, scissors)
Write a program to play this game with the computer.
SNAKE>WATER>GUN>SNAKE
'''

from random import randint as Rand

# defining function to resolve choices
def Play(marker):
    if type(marker)==int:
        if marker==1: play = 'SNAKE'
        elif marker==2: play = 'WATER'
        else: play = 'GUN'
        return play
    elif type(marker)==str:
        if marker.upper() == 'SNAKE': play = 1
        elif marker.upper() == 'WATER': play = 2
        elif marker.upper() == 'GUN': play = 3
        else: pass
        return play

# defining function to determine win/loss/draw for each hand
def PlayHand(comp_x, user_x):
    comp = (Play(comp_x).strip()).upper()
    user = (user_x.strip()).upper()
    play_result = ""
    # win/loss/draw from USER perspective
    if (comp=='SNAKE' and user=='SNAKE') or (comp=='WATER' and user=='WATER') or (comp=='GUN' and user=='GUN'):
        play_result = 'DRAW'
    elif (comp=='SNAKE' and user=='WATER') or (comp=='WATER' and user=='GUN') or (comp=='GUN' and user=='SNAKE'):
        play_result = 'LOSS'
    elif (comp=='SNAKE' and user=='GUN') or (comp=='WATER' and user=='SNAKE') or (comp=='GUN' and user=='WATER'):
        play_result = 'WIN'
    return play_result


# defining function to give icon
def Play_Icon(value_icon:str):
    choice_icon = ''
    value_icon=(value_icon.strip()).upper()
    # \U0001F30A - water wave
    # \U0001F40D - snake
    # \U0001F52B - pistol
    # \U0001F600 - grinning face
    # \U00012639 - frowning face
    # \U0001F62A - sleepy face
    # \U0001F610 - neutral face
    # \U0001F3c6 - trophy
    if value_icon == 'SNAKE':
        choice_icon = '\U0001F40D'
    elif value_icon == 'WATER':
        choice_icon = '\U0001F30A'
    elif value_icon == 'GUN':
        choice_icon = '\U0001F52B'
    elif value_icon == 'WIN':
        choice_icon = '\U0001F3c6'
    elif value_icon == 'LOSS':
        choice_icon = '\U0001F62A'
    elif value_icon == 'DRAW':
        choice_icon = '\U0001F610'
    else:
        pass
    return choice_icon


# defining a function to handle file operations for storing results
def file_op(run, user_choice, comp_choice, play_result):
    play_dict = dict()
    play_dict['PlayRun']=str(run+1)
    play_dict['user']=user_choice
    play_dict['Computer']=Play(comp_choice)
    play_dict['Result']=play_result

    gfile = open('Game_SnakeWaterGun.txt', 'a')
    gfile.write(str(play_dict)+'\n')
    gfile.close()
    return

# defininig a function to read user choice correctly
def UChoice():
    user_choice = input("Enter your choice - (SNAKE / WATER / GUN): ").upper()
    user_choice = user_choice.strip()
    if (user_choice == "SNAKE" or user_choice == "WATER" or user_choice == "GUN"):
        return user_choice
    else:
        return UChoice()





# driver
def main():
    num_loop = 10
    win_count = 0
    print()
    heading = "GAME - SNAKE, WATER, GUN"
    print(f'\n++{heading:-^45}++\n')
    for run in range(num_loop):

        # initialize and playthough each round
        comp_choice = Rand(1,3)
        user_choice = UChoice()
        play_result = PlayHand(comp_choice, user_choice) # users perspective
        if play_result == 'WIN': 
            win_count += 1

        # play output
        mystring1 = f"Computer: {Play_Icon(Play(comp_choice))}"
        mystring2 = f"User: {Play_Icon(user_choice)}"
        mystring3 = f"Result: {Play_Icon(play_result)}"
        print(f'{mystring1.strip():^15}{mystring2.strip():^15}{mystring3.strip():^15}\n')

        # file operation
        file_op(run, user_choice, comp_choice, play_result)

    print('+ {:-^45} +'.format('GAME OVER'))
    print()
    # overall win check
    if win_count >= 5:
        print("Congratulations, Player Wins !! \U0001f600")
        print(f"Wins: {win_count} out of 10 chances")
    else:
        print("Player Loses !! \U0001F62A Try next time")
        print(f"Wins: {win_count} out of 10 chances")


if __name__ == '__main__':
    main()
