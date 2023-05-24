import math

print("Welcome to our banking app!")


def signup():
    global name
    global pin
    name = str(input("Please create your username \n"))
    pin = str(input("Please create your 6-character pin \n"))
    if len(pin) == 6:
        pin = pin
    else:
        print("The pin has to be 6-digits")
        newpin = str(input("Please create your 6-digit pin \n"))
        if len(newpin) != 6:
            print("The pin has to be 6-digits")
            signup()
        else:
            pin = newpin
    print("Thank you " + name + ",your account has been successfully created.")
    quit()


def get_current_balance():
    try:
        with open("balance.txt", "r") as file:
            return float(file.read())
    except FileNotFoundError:
        return 0


def update_current_balance(balance):
    with open("balance.txt", "w") as file:
        file.write(str(balance))


def login():
    global cb
    cb = get_current_balance()
    # name1 represents username
    # pin1 represents users pin
    name1 = str(input("Please enter your username\n"))
    pin1 = str(input("Please enter your pin\n"))
    # Check if name and pin matched
    if name1 == name and pin1 == pin:
        print("Hey " + name + " ,Welcome to our online banking app")
        print("Please choose from the menu down below:")
        listmenu = [
            "1-(Deposit)",
            "2-(Withdraw)",
            "3-(Transfer)",
            "4-(Check-Balance)",
        ]
        for b in listmenu:
            print(b)
        choose = int(input("Please enter the number correlating to your choice\n"))
        d = 0
        w = 0
        if choose == 1:
            d = int(input("Enter deposit amount\n"))
            cb += d
            print("Your current balance is: " + str(cb))
            update_current_balance(cb)
            quit()
        elif choose == 2:
            w = int(input("Enter the amount you'd like to withdraw\n"))
            if w > cb:
                print("Insufficient funds")
                login()
            else:
                cb = cb - w
                print(
                    str(w)
                    + " has been withdrawn from your account"
                    + " and your current balance is: "
                    + str(cb)
                )
                update_current_balance(cb)
                quit()
        elif choose == 3:
            dest = str(input("Please enter the receiver's account number\n"))
            amount = int(input("Please enter the amount\n"))
            if amount > cb:
                print("Insufficient funds")
                login()
            else:
                cb = cb - amount
                print(
                    str(amount)
                    + " has been transferred to account: "
                    + str(dest)
                    + " , your remaining balance is "
                    + str(cb)
                )
                update_current_balance(cb)
                quit()
        elif choose == 4:
            print("Your current balance is: " + str(cb))
            quit()
        else:
            print("Option is not available, back to main menu")
            mainmenu()

    else:
        print("Your username or pin is incorrect, have you created an account?")
        list1 = ["1-(yes)", "2-(no)"]
        for i in list1:
            print(i)
        inp = int(input("Enter your choice below\n"))
        if inp == 1:
            list2 = ["1-(Do you want to log in again?), 2-(You forgot your pin?)"]
            for e in list2:
                print(e)
            answerfromuser = str(input("Please enter your choice\n"))
            answerfromuser = int(answerfromuser)
            if answerfromuser == 1:
                login()
            elif answerfromuser == 2:
                forgotpin()
            else:
                print("Option is not available")
                login()
        elif inp == 2:
            print("Please create your account")
            signup()


def forgotpin():
    recoverpin = str(input("Please create your new 6-digit pin \n"))
    if len(recoverpin) != 6:
        print("The pin has to be 6-digits")
        forgotpin()
    else:
        print("Your new pin has been reset, please log in")
        pin = recoverpin
        login()


def mainmenu():
    option1 = int(input("Choose (1) to sign up, (2) to log in\n"))
    if option1 == 1:
        signup()
    elif option1 == 2:
        login()
    else:
        print("Option is not available")
        mainmenu()
    quit()


def quit():
    answer = str(input("Would you like to continue with your transaction? [y]/[n] \n"))
    if answer == "y":
        login()
    elif answer == "n":
        print("Thank you for using this app!")
    else:
        print("Make sure to enter (y) or (n) to answer, please try again.")
        mainmenu()


signup()


# def depositinterest(p, r, t):
# A = Pe^(rt) the formula to calculate compound interest
# p = float(p)
# r = float(r)
# t = float(t)
# rt = r * t
# e = math.exp(rt)
# calculation
# a = p * e  # future value of deposit/investment.
# return a
