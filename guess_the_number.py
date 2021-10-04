import random


def run():
    ramdom_number = random.randint(1, 100)
    lives = 0

    menu = """ 
    ---Select the difficulty---

    a. Easy   ¯\_(ツ)_/¯ (10 lives)
    b. Medium   (¬‿¬)    (5 lives)
    c. Hard     (•_•)    (3  lives)
     """
    print(menu)
    level =input("Choose the difficulty: ")

    if level == "a":
        lives = 10
        chosen_number = int(input("Write a number from 1 to 100: "))


    elif level == "b":
        lives = 5
        chosen_number = int(input("Write a number from 1 to 100: "))


    elif level == "c":
        lives = 3
        chosen_number = int(input("Write a number from 1 to 100: "))

    else:
        print("Choose a valid option \ (•◡•) /")





    while chosen_number != ramdom_number:
        if chosen_number < ramdom_number:
            print("--Choose a bigger number--")
        else:
            print("--Choose a smaller number--")
        lives -= 1

        if lives == 0:
            print("You lost :(")
            break

        if chosen_number == ramdom_number:
            print("Won!")

        else:
           print("You Have " + str(lives) + " lives")
           chosen_number = int(input("Choose other number: "))





if __name__ == "__main__":
    run()


