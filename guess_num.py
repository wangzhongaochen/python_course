import random

def play_game(num):
    while True:
        a = raw_input("Please input a number: ")
        try:
            a = int(a)
        except ValueError:
            print "Wrong type,Please input numbers!"
            continue
        if a > num:
            print "The number is bigger"
        elif a < num:
            print "The number is smaller"
        else:
            print "You are rigth!"
            break
def main():
    print "================begin game================"
    num = random.randint(0,9)
    play_game(num)
    while True:
        b = raw_input("Continue?: ")
        if b == 'yes':
            num = random.randint(0,9)
            play_game(num)
        elif b == 'no':
            print "=============game over!=============="
            break
        else:
            print "Your choice:yes or no? "
if __name__ == '__main__':
    main()

