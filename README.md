# CTF-writeup-fair-dice
This is my solution to the fair-dice challenge hosted by ENISA Hackfest 2020 16 - 17 November 2020.

```console
jsaw@jsaw:~$ nc 35.242.192.203 30769
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
