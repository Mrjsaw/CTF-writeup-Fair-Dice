# CTF-writeup-fair-dice
This is my solution to the fair-dice challenge hosted by ENISA Hackfest 2020 16 - 17 November 2020.

# Challenge

<img src="https://imgur.com/TX8qhIe.png"></img>

```console
jsaw@jsaw:~/ctf/fair-dice$ nc 35.242.192.203 30769
```
# Round 1

```console
Welcome to a fair dice game.
 - We are going to play some fair rounds. Let's say 101.
 - We both throw one dice. The biggest numbered showed on the dice, wins!
 - The person who wins more rounds from 101, wins that game.
 - If you win too many games in the same session, I am going to alter the game rules to make it fairer for me.
 - If you are going to win four games, I will give you a special code.
 - Note that I am getting bored very fast and I will close this game soon.
Should we start?
Let me show you first 3 dices we are going to play:

Here is the blue dice:

       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  3  xx  6  xx  3  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
Ok?

Here is the yellow dice:

       xxxxxxx
       x     x
       x  5  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  5  xx  5  xx  2  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  2  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  2  x
       x     x
       xxxxxxx
Ok?

Here is the red dice:

       xxxxxxx
       x     x
       x  4  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  4  xx  1  xx  4  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  4  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  4  x
       x     x
       xxxxxxx
Ok?
I am chosing the red dice!
What are you choosing? blue / yellow / red:
```

So for the first round we are presented with a simple dice game, using probibility math and some python we can quickly develop the best strategy:

| Computer | Player |
| -------- | ------ |
| blue | red |
| yellow | blue |
| red | blue |

# Round 2

```console
Time for second game!

You are two lucky, altering rules!
 - We are playing with the same dices.
 - Each one of us selects 1 color of the playing dice.
 - Each one of us throws 2 times the playing dice and add the numbers together.
 - The biggest number wins.
```

In the second round the game and dice are the same except that each player rolls them twice, this changes the strategy:

| Computer | Player |
| -------- | ------ |
| blue | yellow |
| yellow | red |
| red | blue |

# Round 3

```console
Time for third game!

OMG! Again you? You are two lucky, altering rules!
 - We are playing 4 new dices.
 - Same rules as 1st game...
 - You shall not pass!
Let me show you the 4 dices we are going to play:

Here is the blue dice:

       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  3  xx  3  xx  3  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
Ok?$ 

Here is the yellow dice:

       xxxxxxx
       x     x
       x  6  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  6  xx  2  xx  2  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  2  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  2  x
       x     x
       xxxxxxx
Ok?$ 

Here is the red dice:

       xxxxxxx
       x     x
       x  5  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  5  xx  5  xx  1  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  1  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  1  x
       x     x
       xxxxxxx
Ok?$ 

Here is the green dice:

       xxxxxxx
       x     x
       x  0  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  0  xx  4  xx  4  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  4  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  4  x
       x     x
       xxxxxxx
Ok?$ 
```

This round adds a new green die and changes their values, the new strategy becomes:

| Computer | Player |
| -------- | ------ |
| green | red |
| blue | green |
| yellow | blue |
| red | yellow |

# Round 4

```console
Time for fourth game!

... No words ...  You are two lucky, altering rules!
 - We are playing 4 new dices.
 - Same rules as 2nd game...
 - If you beat me one more time, I am going to give you my flag!
```

The final round adds the same rules as round 2 but with the extra die:

| Computer | Player |
| -------- | ------ |
| green | yellow |
| blue | red |
| yellow | blue |
| red | yellow |

And voila we are presented with our flag:
```console
DCTF{7537c933a266a45500c5bd35f20679539f596df9e706dc95fae22d15b812141f}
```
Using some python and pwntools we can automate this:
run script.py to get the solution (as this is RNG based and I didn't do any checks, sometimes the player still loses using the best strategy and the script crashes due to EOFError)
check probs.py to see how I figured out the best strategy and probabilities

