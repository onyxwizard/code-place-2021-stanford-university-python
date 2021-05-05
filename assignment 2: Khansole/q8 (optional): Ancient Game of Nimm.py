#@k
def main():
    stone()

def stone():
    i = 20
    while int(i)!=0:
         for x in range(i):
              c = int(x)%2
              if int(c)==0:
                   print("There are "+str(i)+" stones left")
                   a = input("Player 1 would you like to remove 1 or 2 stones? ")
                   if int(a)==1 or int(a)==2:
                        print("\b")
                        if int(a)==1 and int(i)!=0:
                             i=int(i)-int(a)

                        elif int(a)==2:
                             if int(i)==1:
                                  i=int(i)-1
                                  print("\nPlayer 2 wins!")
                                  exit()
                             else:
                                  i=int(i)-int(a)
        
                        elif int(i) == 0:
                             print("\nPlayer 2 wins!")
                             exit()
                             
                   else:
                       a=input("Please enter 1 or 2: ")
                       print("\b")
                       if int(a)==1:
                            i=int(i)-int(a)

                       elif int(a)==2:
                            if int(i)==1:
                                 i=int(i)-1
                                 print("\nPlayer 2 wins!")
                                 exit()
                            else:
                                 i=int(i)-int(a)
        
                       elif int(i)==0:
                            print("\nPlayer 2 wins!")
                            exit()
#B parameter 
              else:
                   print("There are "+str(i)+" stones left")
                   b = input("Player 2 would you like to remove 1 or 2 stones? ")
                   if int(b)==1 or int(b)==2:
                        print("\b")
                        
                        if int(b)==1 and int(i)!=0:
                             i=int(i)-int(b)
                     
                        elif int(b)==2 and int(i)!=0:
                             if int(i)==1:
                                  i=int(i)-1
                                  print("\nPlayer 1 wins!")                             
                                  exit()
                             else:
                                  i=int(i)-int(b)
                        elif int(i) == 0:
                             print("\nPlayer 1 wins!")                             
                             exit()
                   else:
                        b=input("Please enter 1 or 2: ")
                        print("\b")
                        
                        if int(b)==1 and int(i)!=0:
                             i=int(i)-int(b)
                     
                        elif int(b)==2 and int(i)!=0:
                             if int(i)==1:
                                  i=int(i)-1
                                  print("\nPlayer 1 wins!")                             
                                  exit()
                             else:
                                  i=int(i)-int(b)
                        elif int(i) == 0:
                             print("\nPlayer 1 wins!")                             
                             exit()

if __name__ == '__main__':
    main()
#alternate Code
'''
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
'''
