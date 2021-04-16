database = { }

class Budget():
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(amount, bal):
        bal += amount
        return bal

    def withdraw(user, amount, bal):
        bal -= amount
        return bal

    def balance(db):
        for categ, bal in db.items():
            print(categ, bal)

    def transfer(db, option1, amount, option2):
        value1 = db[option1]
        valuue2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(valuue2) + amount
        return db

def init():
    print("=== **** Welcome to the Budget App**** ===\n")
    Operations()



def Operations():
    try:

        user = int(input("Press (1) To create a new budget\nPress (2) To deposit into a budget\nPress (3) To withdraw from a budget\nPress (4) To check your budget balance\nPress (5) To transfer money between budgets\nPress (6) To quit\n"))
    except:
        print("Invalid option, Try Again")
        Operations()

    if (user == 1):
        new_budget()
    elif (user == 2):
        credit()
    elif (user == 3):
        debit()
    elif (user == 4):
        balance()
    elif (user == 5):
        transfer()
    elif (user == 6):
        out()
    else:
        print("Invalid option, Try Again\n")
        Operations()


def new_budget():
    print("\n=== ***Create New Budget**** ===\n")

    budget_title = input("Enter budget name \n")
    try:
        amount = int(input("Enter your budget amount \n$"))
    except:
        print("\nInvalid input")
        new_budget()
    budget = Budget(budget_title, amount)
    database[budget_title] = amount
    print("")
    print(f"Budget {budget_title} was setup with {amount} ")
    Operations()

def debit():
    print("=== ****Withdraw from a created budget**** ===\n")
    print("**** Available Budgets ****")

    for key, value in database.items():
        print(f"-  {key}")

    pick = int(input("\nPress (1) To continue with your debit transaction\nPress (2) To stop debit transaction\n"))
    if (pick == 1):
        user = input("\n**** Select a budget  to withdraw from ****\n")
        if user in database:
            amt = int(input("Enter amount \n$"))
            if amt < database[user]:
                balance = int(database[user])
                new_balance = Budget.withdraw(user, amt, balance)
                database[user] = new_balance
                print(f"${amt} has been debited from Budget-{user}\nBudget amount remaining ${new_balance}")
                Operations()

            else:
                pick = int(input(f'\nBudget {user} is insufficient of the ${amt} required\nThe actual balance {database[user]}\n\nPress (1) To deposit to the budget\nPress (2) To choose the right budget\n'))
                if (pick == 1):
                    amt = int(input("Enter amount \n$"))
                    balance = int(database[user])
                    new_balance = Budget.deposit(amt, balance)
                    database[user] = new_balance
                    print('')
                    print(f"Budgets {user} has been credited with ${amt}\n")
                    debit()

                elif (pick == 2):
                    debit()
                else:
                    print('Invalid option\n')
                    debit()
        else:
          pick = int(input(f'\n****  Budget {user} does not exist! ****\nPress (1) To create a new budget\nPress (2) To choose the right budget\nPress (3) To move to the menu\n'))
          if (pick == 1):
              new_budget()
          elif (pick == 2):
              debit()
          elif (pick == 3):
              print('')
              Operations()
          else:
              print('Invalid option\n')
              debit()
    elif (pick == 2):
        print('\nYou have terminated the debit transaction ')
        Operations()
    else:
        print('\nInvalid option')
        debit()



def credit():
    print("**** Deposit into a budget ****\n")
    print('**** Available Budgets ****')
    for key, value in database.items():
        print(f"-  {key}")

    pick = int(input('\nPress (1) To continue with your deposit transaction\nPress (2) To stop deposit transaction\n'))
    if (pick == 1):
        user = input("Select a budget \n")
        if user in database:
            amt = int(input("Enter amount \n$"))
            balance = int(database[user])
            new_balance = Budget.deposit(amt, balance)
            database[user] = new_balance
            print(f'\nBudget {user} is credited with ${amt}\nTotal Budget amount is now ${new_balance}')
            Operations()

        else:
            print('')
            pick = int(input(f'Budget {user} does not exist!\nPress (1) To create a new budget\nPress (2) To choose the right budget\nPress (3) To move to the menu\n'))
            if (pick == 1):
                new_budget()
            elif (pick == 2):
                credit()
            elif (pick == 3):
                Operations()
            else:
                print('Invalid option\n')
                credit()

    elif (pick == 2):
        print('\nYou terminated the deposit transaction')
        Operations()
    else:
        print('\nInvalid option')
        deposit()


def balance():
    print("Your balance for each budget are displayed below \n")
    check_bal = Budget.balance(database)
    if (check_bal == None):
        print('')
        Operations()
    else:
        print(f'${check_bal}')
        Operations()

def transfer():
    print('**** Available and Valid Budgets ****')
    for key, value in database.items():
        print(key)
        print('')
    from_budget = input("Which budget are you transferring from? \n")
    if from_budget in database:
        from_amount = int(input("How much do you want to transfer? \n$"))
        if from_amount < database[from_budget]:
            to_budget = input("Enter destination of funds \n")
            if to_budget in database:
                db = Budget.transfer(database, from_budget, from_amount, to_budget)
                print("")
                print(f"You transfered ${from_amount} from {from_budget} to {to_budget} ")
                for key, value in db.items():
                    print(key, value)
                Operations()
            else:
                print(f'\n{from_budget} Budget does not exist, please choose from the valid budget below\n')
                transfer()
        else:
            print(f'You do not have such amount-${from_amount} in {from_budget} budget')
            transfer()
    else:
        print(f'Budget {from_budget} does not exist\n')

        transfer()

def out():
    try:
        pick = int(input('Are you sure you want to quit?\nPress (1) to quit\nPress (2) to continue\n'))
    except:
        print('Invalid input\n')
        out()

    if (pick == 1):
        print("\nThank you.\n Bye for now.")
        quit()
    elif (pick == 2):
        Operations()
    else:
        print('Invalid input\n')
        out()



init()