from tkinter import *
from tkinter import messagebox
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from account import Account
import TextMessages

# This program runs a debt management game. The window has four different phases:
# 1. The first part tells you instructions about how to play the same and asks for you to
#    select the amount of debt accounts you want to manage in the game. The setup for this is
#    at the bottom of the code. When the user is done they click a button that sets up the next
#    page through the move_on function.
#
# 2. The second window then asks for user inputs to say how much debt each account has, the
#    interest of each account, how much money to have in a round, and how much money to have
#    in rounds 6, 12, and 18. When the user is done they click a button that activates the
#    check function. check makes sure all inputs were valid then calls the game function
#    to set up the game. Then it recreates the window.
#
# 3. This third window has the instructions on how to play the game. Then, when the user is ready
#    they can click the start button which will then call the game function and generate the game.
#
# 4. The game function then sets up the game by creating a graph at the top and displays
#    account information as well. It sets up entry boxes so every round the user chooses how much
#    to put into each account. Then the updating_info and graphing functions go about updating
#    the window.

root = Tk()
root.title("Debt Management Game")

# Will hold the number of accounts in the same
var = IntVar()

# An array of the radio button options for picking number of accounts
options = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]

# List of all the names for the possible five accounts
names = ['Account A', 'Account B', 'Account C', 'Account D', 'Account E']

# List of all graph line colors for the graphs of the accounts
colors = ['r-', 'b-', 'g-', 'y-', 'o-']

li = []  # Will hold the entry frames from the second page of the program
values = []  # Hold the values from the entries of the frames stored in li
accounts = []  # Hold all of the accounts objects made
lines = []  # Holds the lines used for the graph
entries = []  # Holds the entry widgets for the amounts the user enters to pay accounts
stats = []  # Holds info for account information to be displayed
calc = []  # Holds the amount of interest each account will generate

# Creates the accounts for the game with a name, amount, and interest rate
def create_accounts():
    x = var.get()
    for i in range(x):
        amt = 0
        ir = 0
        if i == 0:
            amt = values[0]
            ir = values[1]
        elif i == 1:
            amt = values[2]
            ir = values[3]
        elif i == 2:
            amt = values[4]
            ir = values[5]
        elif i == 3:
            amt = values[6]
            ir = values[7]
        elif i == 4:
            amt = values[8]
            ir = values[9]
        acct = Account(names[i], amt, (ir / 100))
        accounts.append(acct)

# Will create initial line on the graph for each account
def create_lines():
    for i in range(len(accounts)):
        x = [0]  # x value is round number
        y = [accounts[i].amount]  # y value is the amount of debt in the account
        z = [x, y]
        lines.append(z)


CURRENT_CASH_NORMAL = 0  # The amount of cash the user has to pay debts for a round, initialized to zero
current_cash = 0  # The amount of cash the user has at a specific round, initialized to zero
round_number = 1
# Set FINAL_ROUND to one larger than the number of rounds you really want
FINAL_ROUND = 23

# Rounds 6, 12, and 18 the user can get a bonus and this list holds those values, all initialized to zero
round_bonuses = [0, 0, 0]

# This function creates the main game page and updates it
def game():
    for ele in root.winfo_children():
        ele.destroy()
    global CURRENT_CASH_NORMAL
    global current_cash
    current_cash = CURRENT_CASH_NORMAL
    global round_number
    round_number = 1
    create_accounts()
    SIZE = len(accounts)  # This constant refers to the number of accounts in the game

    # Setting up the graph
    f = Figure(figsize=(16, 4), dpi=100)
    a = f.add_subplot(111)
    create_lines()
    for i in range(SIZE):
        a.plot(lines[i][0], lines[i][1], colors[i], marker='o', label=names[i])
    a.legend(loc="upper right")
    a.set_xlabel('Round Number')
    a.set_ylabel('Amount of Debt')
    starting_max = 0
    for ac in accounts:
        if ac.amount > starting_max:
            starting_max = ac.amount

    a.set_xbound(lower=0, upper=25)
    a.set_ybound(lower=0, upper=starting_max + 10000)
    a.grid()
    canvas = FigureCanvasTkAgg(f, root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)

    # Setting up the frame that holds the location to make payments and other account info
    frame = Frame(root, bd=5)
    frame.grid(row=4, column=0, sticky='W')
    header = Label(frame, text="Accounts:")
    header.grid(row=1, column=0, padx=5, columnspan=2)
    header2 = Label(frame, text="Debt in Each Account:")
    header2.grid(row=1, column=3, padx=5, columnspan=2)
    header3 = Label(frame, text="Interest Amount:")
    header3.grid(row=1, column=5, padx=5, columnspan=1)

    # This loop creates an entry box to pay each account (e1), a label on the information on the amount of money
    # and interest rate (b1), and another label with the amount of interest each account will incur (c1)
    for i in range(SIZE):
        a1 = Label(frame, text=names[i])
        a1.grid(row=i+2, column=0, sticky='E')
        e1 = Entry(frame)
        e1.grid(row=i+2, column=1, sticky='W')
        entries.append(e1)
        pt1 = names[i]+": " + "{:.2f}".format(accounts[i].amount)
        pt2 = pt1 + '   ' + "{:.2f}".format(accounts[i].rate*100) + "% interest"
        b1 = Label(frame, text=pt2)
        b1.grid(row=i+2, column=3, sticky='W')
        stats.append(b1)
        c1 = Label(frame, text=accounts[i].format_interest())
        c1.grid(row=i+2, column=5, sticky='E')
        calc.append(c1)

    # round_indicator: Tells the player what the round number is
    # amount_available: Tells the user how much money they have this round
    round_indicator = Label(root, text="Round number: " + str(round_number))
    amount_available = Label(root, text="Amount available: " + "{:.2f}".format(current_cash))
    round_indicator.grid(row=2, column=1, sticky='W')
    amount_available.grid(row=3, column=1, sticky='W')

    # Creates a popup when the game is done which displays the amount of debt the player had left
    def game_over_message():
        popup = Tk()

        def leave_popup():
            popup.destroy()

        popup.title("Game over")
        end_amount = 0
        for i in range(SIZE):
            end_amount += accounts[i].amount
        end_total = "{:.2f}".format(end_amount)
        msg = "Congrats! You finished the game. Your total debt remaining was " + end_total
        lab = Label(popup, text=msg)
        lab.pack()
        exit_button = Button(popup, text='Okay', command=leave_popup)
        exit_button.pack()
        popup.mainloop()

    # Called when the player goes to the next round, the function updates the screen
    def update_info():
        # Checking that the user put in valid values
        global current_cash
        try:
            for i in range(SIZE):
                x = float(entries[i].get())
        except:
            messagebox.showerror("Error", "Please input valid numbers only")
            return

        for i in range(SIZE):
            if float(entries[i].get()) < 0:
                messagebox.showerror("Error", "Please do not input values less than zero")
                return

        total_spent = 0
        for i in range(SIZE):
            total_spent += float(entries[i].get())

        if total_spent > current_cash:
            messagebox.showerror("Error", "Please do not spend more money than you have available")
            return

        if total_spent != current_cash:
            messagebox.showerror("Error", "You must spend all available money")
            return

        # Payments is a list of the amount the player paid to each account in the round
        payments = []
        for i in range(SIZE):
            payments.append(float(entries[i].get()))

        # The graphing function takes care of updating the graph
        graphing(payments)
        # Clears the entry frames
        for i in range(SIZE):
            entries[i].delete(0, END)
        # Updates the round number, unless it was the final round
        if round_number != FINAL_ROUND:
            round_indicator.config(text="Round number: " + str(round_number))
        # Updates information on the accounts
        for i in range(SIZE):
            pt1 = names[i] + ": " + "{:.2f}".format(accounts[i].amount)
            pt2 = pt1 + '   ' + "{:.2f}".format(accounts[i].rate * 100) + "% interest"
            stats[i].config(text=pt2)
            calc[i].config(text=accounts[i].format_interest())

        # Checks if the round is going to be 6, 12, or 18 and sets the amount of money the player has accordingly
        if round_number % 18 == 0:
            current_cash = round_bonuses[2]
            amount_available.config(text="Amount available: " + "{:.2f}".format(current_cash))
        elif round_number % 12 == 0:
            current_cash = round_bonuses[1]
            amount_available.config(text="Amount available: " + "{:.2f}".format(current_cash))
        elif round_number % 6 == 0:
            current_cash = round_bonuses[0]
            amount_available.config(text="Amount available: " + "{:.2f}".format(current_cash))
        else:
            current_cash = CURRENT_CASH_NORMAL
            amount_available.config(text="Amount available: " + "{:.2f}".format(current_cash))

        # Ends the game if there are no more rounds left
        if round_number == FINAL_ROUND:
            game_over_message()

        # Ends the game if there is no more debt left
        total_debt = 0
        for i in range(SIZE):
            total_debt += accounts[i].amount
        if total_debt == 0:
            round_indicator.config(text="Round number: " + str(round_number - 1))
            game_over_message()

    # Creates the button that confirms the payments and moves to the next round
    button1 = Button(frame, text="Pay Debts", command=update_info)
    button1.grid(row=SIZE+2, column=1, sticky='W')

    # Updates the graph each round where payments is a list of values that says
    # how much the player into each account
    def graphing(payments):
        global round_number
        # remaining_debt is the debt in each account after each one has been paid
        remaining_debt = []
        for i in range(SIZE):
            remaining = accounts[i].make_payment(payments[i])
            remaining_debt.append(remaining)
        for i in range(SIZE):
            lines[i][0].append(round_number)
            lines[i][1].append(remaining_debt[i])

        for i in range(SIZE):
            a.plot(lines[i][0], lines[i][1], colors[i], marker='o', label=names[i])
        a.set_xlabel('Round Number')
        a.set_ylabel('Amount of Debt')
        a.set_xbound(lower=0, upper=25)
        a.set_ybound(lower=0)
        canvas = FigureCanvasTkAgg(f, root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)

        # Increments the round number the game is on
        # Disables the next round button (button1) if the game is over
        round_number += 1
        if round_number == FINAL_ROUND:
            button1.config(state=DISABLED)
        total_debt = 0
        for i in range(SIZE):
            total_debt += accounts[i].amount
        if total_debt == 0:
            button1.config(state=DISABLED)

# Checks that user inputted data correctly and then starts the game
def check():
    # Check that the user only inserted valid inputs
    try:
        for i in li:
            test = float(i.get())
    except:
        messagebox.showerror("Error", "Please input valid numbers only")
        return

    for i in li:
        if float(i.get()) < 0:
            messagebox.showerror("Error", "Please do not input values less than zero")
            return

    # Stores the amount the user gets for round 6, 12, and 18 for later use
    round_bonuses[2] = float(li.pop().get())
    round_bonuses[1] = float(li.pop().get())
    round_bonuses[0] = float(li.pop().get())

    global CURRENT_CASH_NORMAL
    # Stores the amount the user gets in a regular round for later use
    CURRENT_CASH_NORMAL = float(li.pop().get())

    # Stores the information the user entered for each account in a list that will be used to make the accounts
    for i in li:
        val = float(i.get())
        values.append(val)

    # Give instructions how to play the game
    for ele in root.winfo_children():
        ele.destroy()

    def start_game():
        game()

    instructions = TextMessages.instructions()
    instr = Message(root, text=instructions, anchor=W, aspect=450)
    instr.grid(row=0)

    # The start button will start the game when clicked
    button2 = Button(root, text="Start", command=lambda: start_game(), width=10)
    button2.grid(row=1)

# Updates the start window to now ask about information for the accounts before the game starts
def move_on():
    # Checks that the user selected a number of accounts
    if var.get() == 0:
        messagebox.showerror("Error", "Please select a number")
        return
    for ele in root.winfo_children():
        ele.destroy()
    msg = TextMessages.entry_explain()
    explain = Message(root, text=msg, width=450)
    explain.grid(row=0, columnspan=3, sticky=W)
    h1 = Label(root, text='Account')
    h1.grid(row=1, column=0)
    h2 = Label(root, text='Amount')
    h2.grid(row=1, column=1)
    h3 = Label(root, text='Interest Rate')
    h3.grid(row=1, column=2)

    amt = var.get()
    # For each account sets up two entry widgets for the user to enter the amount and interest rate for each account
    # Then, it adds those entry widgets to the list li for later access
    for i in range(amt):
        lab = Label(root, text=names[i])
        lab.grid(row=i + 2, column=0)
        amount_entry = Entry(root)
        interest_entry = Entry(root)
        amount_entry.grid(row=i + 2, column=1, padx=2)
        interest_entry.grid(row=i + 2, column=2, padx=2)
        li.append(amount_entry)
        li.append(interest_entry)

    # Sets up an entry for the player to user how much money they get in a regular round
    money_per_round = Label(root, text="Normal Round")
    money_per_round.grid(row=i+3, column=0, pady=(5, 0))
    money_entered = Entry(root)
    money_entered.grid(row=i+3, column=1, pady=(5, 0))
    li.append(money_entered)

    # Sets up an entry for the player to user how much money they get in round 6
    money_round6 = Label(root, text="Round 6")
    money_round6.grid(row=i + 4, column=0)
    money_entered2 = Entry(root)
    money_entered2.grid(row=i + 4, column=1)
    li.append(money_entered2)

    # Sets up an entry for the player to user how much money they get in round 12
    money_round12 = Label(root, text="Round 12")
    money_round12.grid(row=i + 5, column=0)
    money_entered3 = Entry(root)
    money_entered3.grid(row=i + 5, column=1)
    li.append(money_entered3)

    # Sets up an entry for the player to user how much money they get in round 18
    money_round18 = Label(root, text="Round 18")
    money_round18.grid(row=i + 6, column=0)
    money_entered4 = Entry(root)
    money_entered4.grid(row=i + 6, column=1)
    li.append(money_entered4)

    # This button allows the player to continue the game once they put in all of the information
    enter_data = Button(root, text="Continue", command=check, width=10, borderwidth=4)
    enter_data.grid(row=i + 7, column=1)

# Instructions that appear when you start the game
words = TextMessages.starting_text(FINAL_ROUND)
message = Message(root, text=words, anchor=W, aspect=450)
message.grid(row=0)

# Creates the radio button that lets you select how many accounts the game will have
j = 1
for txt, amount in options:
    r = Radiobutton(root, text=txt, variable=var, value=amount)
    r.grid(row=j, sticky='w')
    j += 1

# Allows you to move from the start page to the next page and set up the account and game information
button = Button(root, text="Continue", command=lambda: move_on(), width=10)
button.grid(row=j+1)

root.mainloop()