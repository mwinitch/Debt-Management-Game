# Debt Management Game

Welcome to the debt management game! In this game you have to manage a series of debt accounts. Each round, you are given some amount of money and you get to decide how much money to put into each debt account. When you launch the game you get to decide how many debt accounts there are. Then, you say how much debt you want in each account and its interest rate. You also decide how much money you receive each round, and can even choose to receive a bonus in certain rounds. The program uses tkinter for the GUI and Matplotlib to create the graph.

This project is made from the following files .py files:
1. DebtGame
   * The main file that creates and runs the game. Creates and updates the GUI with tkinter
2. account
   * Holds information about each debt account and functions to perform on the debt accounts
3. TextMessages
   * Holds all of the messages and instructions that DebtGame needs to put on the screen

## How to play the game

When you start the game, you get to choose how many debt accounts you want to play with. After you confirm that selection, you then get to set up some information about the game. You choose how much debt is in each account and the interest rate of each account. Then you choose how much money you will receive in a round. You also get to set how much you receive in rounds 6, 12, and 18, allowing to give yourself a possible bonus if you so choose. When this is all setup you can start the game.

The game is played for 22 rounds, or until all of the debt is paid off. Each round, you are given a certain amount of money. You choose how much money to put toward each debt account. You must spend all of the money you are given, you can not save. If you do not wish to put any money into a specific account just enter 0 for that account. You will also be able to see the graph which will show you how much debt you have in each account over the course of the game. You will then click a button that confirms your payments for that round. This will update the graph and other information in each account.     
