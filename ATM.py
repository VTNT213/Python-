import random

print("WELCOME TO PYTHON BANK ATM!")
restart = ('Y')
chances = 3
balance = random.randint(1111,9999)

while chances >= 0:
    pin = int(input("Please Enter you 4 digit PIN: "))
    if pin == (6969):
        print("You've entered the correct pin.")
        print("Please Press 1 to check your balance.")
        print("Please Press 2 to make a Withdrawal.")
        print("Please Press 3 to Pay in")
        print("Please Press 4 to Return card \n")

        while restart not in('n', 'N', 'NO', 'no'):
            print("Please press 1 for your Balance")
            print("Please press 2 to make a Withdrawal")
            print("Please press 3 to Pay in.")
            print("Please press 4 to return card.")
        option = int(input("What would you like yo choose?: "))
        if option == 1:
            print("Your balance is $", balance)
            restart = input("Would you like to go back? ")
            if restart in('n', 'N', 'NO', 'no'):
                print("Thank you!")
                break
            elif option == 2:
                option2 = ('Y')
                withdrawal = float(input("How much would you like to Withdraw? 10, 20, 40, 60, 80, 100 for other enter 1:"))
                if withdrawal in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawal
                    print('\nYour balance is now $', balance)
                    restart = input("Would like to go back? ")
                    if restart in ('n', 'N', 'NO', 'no'):
                        print("Thank You")
                        break
                    elif withdrawal != [10, 20, 40, 60 ,80, 100]:
                        print("Please enter a valid amount.")
                        restart = ('Y')
                    elif withdrawal == 1:
                        withdrawal = float(input("Please enter desired amount: "))
                elif option == 3:
                    Pay_in = float(input("How much would you like to withdraw?: "))
                    balance = balance + Pay_in
                    print("\nYour balance is now $", balance)
                    restart = input("Would you like to go back? ")
                if restart in ('n', 'N', 'NO' 'no'):
                    print("Thank You!")
                    break
                elif option == 4:
                    print("Please wait whilst your card is returnd...\n")
                    print("Thank you for your service!")
                    break
                else:
                    print("Please Enter a correct number. \n")
                    restart('Y')
            elif pin != ('1234'):
                print("Incorrect PIN!")
                chances = chances + 1
                if chances == 0:
                    print("\nNo more tries left!")
                    break







