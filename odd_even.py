import random
import time


def play():
    USER = 0
    COMP = 1

    BAT_FIRST = None

    print("Welcome all to this Hand Cricket Game!\nWe are ready for the toss!\nUser to call...")
    user_call = input("odd or even?\n")
    comp_call = None
    if user_call == "even":
        user_call = 0
        comp_call = 1
    elif user_call == "odd":
        user_call = 1
        comp_call = 0
    print("Tossing ...")
    time.sleep(1)
    toss = random.randint(0, 1)
    if toss == 1:
        print("It is odd")
    else:
        print("It is even")
    if toss == user_call:
        t = input("You won the toss.\nYou want to Bat or Bowl?\n")
        print(f"User won the toss and elected to {t} first")
        if t.lower() == 'bat':
            BAT_FIRST = USER
        else:
            BAT_FIRST = COMP
    else:
        if random.randint(0, 1) == 0:
            BAT_FIRST = COMP
            print("Comp wants to Bat First")
        else:
            BAT_FIRST = USER
            print("Comp wants to Bowl First")

    score_1 = 0
    score_2 = 0

    OUT = False

    while OUT == False:
        user_input = int(input("Your input : ").strip())
        comp_input = random.randint(1, 6)
        print(f"Computer Input : {comp_input}")
        if user_input == comp_input:
            print(
                f"OUT!\n{'Computer' if BAT_FIRST == USER else 'User' } needs {score_1 +1 } Runs to win!\n")
            OUT = True
            break
        else:
            if BAT_FIRST == USER:
                score_1 += user_input
            else:
                score_1 += comp_input
            print(f"Score : {score_1}")

    OUT = False

    while OUT == False:
        user_input = int(input("Your input : ").strip())
        comp_input = random.randint(1, 6)
        print(f"Computer Input : {comp_input}")
        if user_input == comp_input:
            print(f"OUT!\n {'User' if BAT_FIRST == USER else 'Computer'} Wins")
            OUT = True
        else:
            if BAT_FIRST == USER:
                score_2 += comp_input
            else:
                score_2 += user_input
            print(f"Score : {score_2}")
            print(f"Need {(score_1 - score_2)+1} more to win")
        if score_2 > score_1:
            print(f"{'User' if BAT_FIRST == COMP else 'Computer'} Wins")
            break

    print("Play Again? Y/N\n")
    if input().lower() == 'y':
        play()
    else:
        print("See you soon!")


if __name__ == "__main__":
    play()
