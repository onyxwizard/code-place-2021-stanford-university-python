# (optional) Extension

Since extensions are open ended and may consist of different files, we use the Terminal instead here.

To run your extensions, type python file.py into the Terminal, where file.py could be nimm2.py etc.

You can also press the up and down arrow keys in the Terminal to cycle through recent commands.

There are no test cases, so Submit when you're ready.
Optional Extensions

Once you’ve completed all the required parts of the assignment, you might want to consider adding some extensions. Extensions, you may recall, are things that are totally optional. Here are some extra programs to write if you are interested – but feel free to just make something cool!
Extend Khansole Academy

You could consider extending your Khansole Academy program to, for example, add more problem types (subtraction, multiplication, division, and more). You could also consider problems beyond arithmetic. If you could build your own version of Khansole Academy, what would you use it to help people learn? Be creative and enjoy.
AI for Game of Nimm

Can you make a computer player that can always win in a game of Nimm?
Hailstones

A separate (optional) problem you could consider writing is based on a problem in Douglas Hofstadter’s Pulitzer-prize-winning book Gödel, Escher, Bach. That book contains many interesting mathematical puzzles, many of which can be expressed in the form of computer programs. In Chapter XII, Hofstadter mentions a wonderful problem that is well within the scope of what you know. The problem can be expressed as follows:
```
Pick some positive integer and call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
```
On page 401 of the Vintage edition of his book, Hofstadter illustrates this process with the following example, starting with the number 15:
```
15 is odd, so I make 3n+1: 46
46 is even, so I take half: 23
23 is odd, so I make 3n+1: 70
70 is even, so I take half: 35
106 is even, so I take half: 53
53 is odd, so I make 3n+1: 160
160 is even, so I take half: 80
80 is even, so I take half: 40
40 is even, so I take half: 20
20 is even, so I take half: 10
10 is even, so I take half: 5
5 is odd, so I make 3n+1: 16
16 is even, so I take half: 8
8 is even, so I take half: 4
4 is even, so I take half: 2
2 is even, so I take half: 1
```
As you can see from this example, the numbers go up and down, but eventually—at least for all numbers that have ever been tried—comes down to end in 1. In some respects, this process is reminiscent of the formation of hailstones, which get carried upward by the winds over and over again before they finally descend to the ground. Because of this analogy, this sequence of numbers is usually called the **Hailstone sequence**, although it goes by many other names as well.
You might want to write a Python program that reads in a number from the user and then displays the Hailstone sequence for that number, just as in Hofstadter’s book, followed by a line showing the number of steps taken to reach 1. For example, here’s a sample run of what such a program might look like (user input is in **bold italics**):
```
Enter a number: 17
17 is odd, so I make 3n + 1: 52
52 is even, so I take half: 26
26 is even, so I take half: 13
13 is odd, so I make 3n + 1: 40
40 is even, so I take half: 20
20 is even, so I take half: 10
10 is even, so I take half: 5
5 is odd, so I make 3n + 1: 16
16 is even, so I take half: 8
8 is even, so I take half: 4
4 is even, so I take half: 2
2 is even, so I take half: 1
The process took 12 steps to reach 1
```
