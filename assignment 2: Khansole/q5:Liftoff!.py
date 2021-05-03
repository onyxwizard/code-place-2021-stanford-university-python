"""
Prints out a spaceship launch sequence.
"""

def main():
    num=11
    for i in range(10):
        num=int(num)-1
        print(num)
    print("Liftoff!")

if __name__ == '__main__':
    main()
