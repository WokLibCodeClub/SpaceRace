# Ending the game

## Losing the game

We have a `lives` variable, let us end the game when that gets to zero. Add the following to the main loop
just before the `screen.update()` and fill in the variable name of `XXX`:

```python
  if XXX == 0:
    game_over()
```

<details><summary>Show solution</summary>

```python
  if lives == 0:
    game_over()
```
</details>

Hopefully this makes sense, when the number of lives is zero, we call the function called `game_over`.
However, we need to define the `game_over` function. I will give you most of the code for this function
but there is one important value that I will miss out:

```python
def game_over():
  t = Turtle()
  t.hideturtle()
  t.color("red")
  t.goto(0,0)
  t.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
  global playing
  playing = XXX
```

This creates a turtle, with red text which writes "GAME OVER" in the centre of the screen. This function also
modifies a global variable called `playing`. This variable should be either `True` or `False`, what do you think
`playing` should be if the game is ending. Hopefully you said `False`! If so, then you were right, `playing` should be `False`
if it is game over. This will exit the main loop and finish the code. If you try playing and collide with an asteroid 3 times then
you should see the game over message and the game should stop.

## Winning the game

The previous instructions say how to end the game by losing all the lives. Now let's add some code to be able to win the game 
when the player gets a score of 3. Put this code in the main loop just after the check for `lives == 0`, what number will you put 
in for `XXX`:

```python
  if score == XXX:
    player_wins()
```

Now define the `player_wins` function, this is very similar to the `game_over` function. Copy and paste the `game_over` function and
rename the function `player_wins`. Now change the text colour from "red" to "lime", and change the message from "GAME OVER" to "YOU WIN".
Solution below:

<details><summary>Show solution</summary>

```python
def player_wins():
  t = Turtle()
  t.hideturtle()
  t.color("lime")
  t.goto(0,0)
  t.write("YOU WIN!!!!!", align="center", font=("Arial", 40, "bold"))
  global playing
  playing = False
```
</details>

Now the game should end when the player gets to a score of 3!

## Tidy up end-game message

Currently, the "GAME OVER" or "YOU WIN" message could be overlapping with asteroids. It would be nice to delete the asteroids that are
overlapping when the message shows. Add the following function:

```python
def clear_rocks_for_message():
  for rock in rocks:
    if rock.ycor() < 50 and rock.ycor() > -10:
      rock.hideturtle()
```

This hides the rocks if they are in the area of the end-game message.

Finally, call this function after either of the end-game messages is written i.e. put the following line after `playing = False` in each of `game_over` and `player_wins`:

```python
clear_rocks_for_message()
```

And that's the end of this project! You should now have a functioning space race game coded in python.
