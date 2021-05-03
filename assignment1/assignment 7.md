# Q7: Midpoint (optional!)

As an exercise in solving algorithmic problems, program Karel to place a single beeper at the middle of 1st Street (aka Row). For example, say Karel starts in the 5x5 world pictured in the figure:

<img src="/images/assignment 7.jpeg">

Karel should end with Karel standing on a beeper in the following position:

<img src="/images/assignment 71.jpeg">

Note that the final configuration of the world should have only a single beeper at the midpoint of 1st Street. Along the way, Karel is allowed to place additional beepers wherever it wants to, but must pick them all up again before it finishes. Similarly, if Karel paints/colors any of the corners in the world, they must all be uncolored before Karel finishes.

In solving this problem, you may count on the following facts about the world:

    Karel starts at the bottom left corner, facing east, with an infinite number of beepers in its bag.

    The initial state of the world includes no interior walls or beepers.

    The world need not be square, but you may assume that it is at least as tall as it is wide.

Your program, moreover, can assume the following simplifications:

    If the width of the world is odd, Karel must put the beeper in the center square. If the width is even, Karel may drop the beeper on either of the two center squares.

    It does not matter which direction Karel is facing at the end of the run.

There are many different algorithms you can use to solve this problem so feel free to be creative!

You should make sure your program runs successfully in all of the following worlds (which are just a few different examples to test out the generality of your solution): Midpoint.w (default world), Midpoint1.w, Midpoint2.w, Midpoint8.w .

You can toggle between worlds by changing Midpoint.w in the last line of the file (which is currently **run_karel_program('Midpoint.w')** to the filename of your choice (make sure to include the quotation marks around the filename) and running your program.
