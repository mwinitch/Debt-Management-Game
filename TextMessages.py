# This class holds all of the text messages used in the debt game that explain and give information to
# the user. The main file DebtGame.py uses these messages to put into message widgets.

def starting_text(round):
    words = "Welcome to the debt management game. Over the course of " + str(round - 1) + " rounds, you will be " \
            "playing a debt management simulator. Every round, you will decide how to allocate your money to pay " \
            "off your debts. Before we can start, choose how many debt accounts you want to have, " \
            "then click continue."
    return words

def entry_explain():
    msg = "For each account enter how much debt you want it to have and " \
          "the interest rate of each account. If you want an account to have an interest " \
          "rate of 3.5%, just input 3.5 for that account. Also enter a value for how " \
          "much money you want in a regular round. Rounds 6, 12, and 18 are special " \
          "rounds where you can choose how much money you want in those rounds. Do not put commas in " \
          "any of your numbers. Click continue when you are done."
    return msg

def instructions():
    instructions = "You are now ready to start the game. Each round, you will be given a certain " \
                   "amount of money that is available for you to use. You will see all of your accounts " \
                   "and how much debt is in each. You will also see how much in interest each account will " \
                   "generate. Every round, enter how much you want to put into paying each debt account. You must " \
                   "spend ALL the money you have in a given round, you are not allowed to save. If you not " \
                   "want to put any money in an account for a round, enter 0 for that account. When you have " \
                   "finalized your choices for the round click 'Pay Debts' to move to the next round. Do not put " \
                   " commas in any of your numbers. Click start when you are ready. Good luck!"
    return instructions