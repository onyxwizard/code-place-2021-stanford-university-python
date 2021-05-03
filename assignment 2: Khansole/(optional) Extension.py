"""
TODO: Write a description here
"""

import random 
bold = '\033[1m'
italic = '\033[3m'
end = '\033[0m'

def main():
    hail()

def hail():
    count = 0
    user = input("Enter a number: "+bold+italic)
    #print("\t"+end)
    while user!=1:
        count=int(count)+1
        x=int(user)%2
        if x==0:
            print(end+str(user)+" is even, so I take half: ",int(int(user)/2))
            user = int(user)/2
        else:
            print(end+str(user)+" is odd, so I make 3n + 1: ",int(3*(int(user))+ 1))
            user =3*(int(user))+ 1
    print("The process took "+str(count)+" steps to reach 1")
if __name__ == "__main__":
    main()
