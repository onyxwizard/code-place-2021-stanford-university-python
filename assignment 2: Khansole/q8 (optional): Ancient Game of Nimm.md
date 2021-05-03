# Q8 (optional): Ancient Game of Nimm

Tip! First work on breaking down the problem into small parts, and solving each of the milestones.

Once you're ready to submit, click the Run button to make sure you code works, and then click Submit.

Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left.

The game of Nimm goes as follows:

    The game starts with a pile of 20 stones between the players.

    The two players alternate turns.

    On a given turn, a player may take either 1 or 2 stone from the center pile.

    The two players continue until the center pile has run out of stones.

The last player to take a stone loses. Here's a sample execution:
```
There are 20 stones left
Player 1 would you like to remove 1 or 2 stones? 2

There are 18 stones left
Player 2 would you like to remove 1 or 2 stones? 2

There are 16 stones left
Player 1 would you like to remove 1 or 2 stones? 1

There are 15 stones left
Player 2 would you like to remove 1 or 2 stones? 2

There are 13 stones left
Player 1 would you like to remove 1 or 2 stones? 2

There are 11 stones left
Player 2 would you like to remove 1 or 2 stones? 1

There are 10 stones left
Player 1 would you like to remove 1 or 2 stones? 2

There are 8 stones left
Player 2 would you like to remove 1 or 2 stones? -1
Please enter 1 or 2: 2

There are 6 stones left
Player 1 would you like to remove 1 or 2 stones? 2

There are 4 stones left
Player 2 would you like to remove 1 or 2 stones? 2

There are 2 stones left
Player 1 would you like to remove 1 or 2 stones? 1

There are 1 stones left
Player 2 would you like to remove 1 or 2 stones? 1

Player 1 wins!
```
Write a program to play Nimm. To make your life easier we have broken the problem down into smaller milestones. You have a lot of time for this program. Take it slowly, piece by piece.
# Milestone 1
Start with 20 stones. Repeat the process of removing stones and printing out how many stones are left until there are zero. Don't worry about whose turn it is. Don't worry about making sure only one or two stones are removed. Use the method input(msg) which prints msg and waits for the user to enter an input. Make sure to convert the input into an int.
```
There are 20 stones left
Would you like to remove 1 or 2 stones? 2

There are 18 stones left
Would you like to remove 1 or 2 stones? 17

There are 1 stones left
Would you like to remove 1 or 2 stones? 3

Game over
```
# Milestone 2

Create a variable of type int to keep track of whose turn it is (remember there are two players). Tell the user whose turn it is. Each time someone picks up stones, change the player number.
```
There are 20 stones left
Player 1 would you like to remove 1 or 2 stones? 1

There are 19 stones left
Player 2 would you like to remove 1 or 2 stones? 1

There are 18 stones left
Player 1 would you like to remove 1 or 2 stones? 17

There are 1 stones left
Player 2 would you like to remove 1 or 2 stones? 1

Game over
```
# Milestone 3

Make sure that each turn only one or two stones are removed. After you read a number of stones to remove from a user (their input), you can use the following pattern to check if it was valid and keep asking until it is valid.
```
while inputisinvalid:
    amount = int(input("Please enter 1 or 2: "))
 ```
 As a final touch, announce the winner after the game is over.
