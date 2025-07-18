# Tryna create a Guess The Number Game
import random 
num = random.randint(1,100)
Max_guess = 10
a=0
def main():
    print("Welcome To Guess The Number Game")
    print("guess the number u just have 10 guess".title())
    while True:
        global a
        a+=1
        print(f"Guess#{a}: ")
        guess = int(input(" "))
        if guess > num:
                print ("too high".title())
        if guess < num:
                print ("too low".title())
        if guess == num:
                print(f"you guessed it correctly!!!! it's {num} ")
                break
        global Max_guess
        Max_guess -=1
        if Max_guess == 0:
            print("u have no more chance to guess".title())
            break
main()
