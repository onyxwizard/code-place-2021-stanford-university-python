"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
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
    r = random.randint(mini,maxi)
    q = random.randint(mini,maxi)
    print("what is "+str(r)+" + "+str(q)+"?")
    sumup= r + q
    user=input("Your answer: "+bold+italic)
    if int(sumup) == int(user):
        print("\033[0m"+"Correct!")
    else:
        print("\033[0m"+"Incorrect. The expected answer is "+str(sumup))


if __name__ == '__main__':
    main()
