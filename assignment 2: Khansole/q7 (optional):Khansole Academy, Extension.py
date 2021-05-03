"""
TODO: Write a description here
"""

#bold \033[1m
#italic \033[3m
import random
bold = '\033[1m'
italic = '\033[3m'
end = '\033[0m'

def main():
    add()
    

def add():
    mini = 10
    maxi = 99
    e = 0
    for i in range(3):
        r = random.randint(mini,maxi)
        q = random.randint(mini,maxi)
        print("What is "+str(r)+" + "+str(q)+"?")
        sumup= r + q
        user=input("Your answer: "+bold+italic)
        if int(sumup) == int(user):
            e=e+1
            print("\033[0m"+"Correct! You've gotten "+str(e)+" correct in a row.")
        else:
            print("\033[0m"+"Incorrect. The expected answer is "+str(sumup))
    if int(e) !=3:
        add()
    else:
        print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()
