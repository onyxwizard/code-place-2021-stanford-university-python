
import random

def main():
    #number of stones at beginning of game
    No_of_Stones = 20
    #tracking palyer1 and player2
    tracking = True
    
    while No_of_Stones > 0:

        if tracking:
            print("There are", No_of_Stones, "stones left")
            stones_left_1=int(input("Player 1 would you like to remove 1 or 2 stones? "))
            while stones_left_1 < 1 or stones_left_1 > 2:
                 stones_left_1 = int(input("Please enter 1 or 2: "))
            No_of_Stones -=  stones_left_1
            tracking = False
            print()
        else:
            print("There are", No_of_Stones, "stones left")
            stones_left_2=int(input("Player 2 would you like to remove 1 or 2 stones? "))
            while stones_left_2 < 1 or stones_left_2 > 2:
                 stones_left_2 = int(input("Please enter 1 or 2: "))
            No_of_Stones -=   stones_left_2
            tracking = True
            print()
        
    if tracking:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")



if __name__ == '__main__':
    main()
