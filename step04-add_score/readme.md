# Adding a score to the game

## The `score` variable

Up to now, we have a rocket, some asteroids, and the rocket can be hit by the asteroids and be sent to the start.
Let's add some code to allow the game to keep track of the score, where the player gets one point if they make it
to the top of the screen.

In the scores section of the starter code, can you create a variable called `score` and initialise it, what number
should you start a score at!? No trick question , it is a simple one line to answer this question:

```python
score = 0
```

Now we need the score to increase if the rocket gets to the end of the screen. Where do you think we'll need to put the
code for checking if the rocket got to the end of the screen? There's somewhere that I previously mentioned is always
cycling and checking things... it is the main loop. We can add a check to the loop to see if the rocket has made it to
the top, but how could we determine if the rocket is at the top? We know the size of the screen, the
coordinate system is 400 x 400, the y-axis runs from -200 to +200. Therefore, if we can get the y-coordinate of the rocket
then we can check if it is at the top. The following code shows how to check the y-coordinate and compare against the maximum y-coordinate.
See if you can complete the TODO in the code:

```python
  if rocket.ycor() > YMAX:
    reset_rocket()
    # TODO Add code to increase the score variable by 1
```

<details><summary>Show solution</summary>

```python
  if rocket.ycor() > YMAX:
    reset_rocket()
    score = score + 1
	# Python also has a special way to write the code above, the line below does exactly the same as the above:
	# score += 1
```
</details>

Be careful about the indentation here. We do not need to check the position of the rocket everytime we move a rock so we do not want the code
to be inside the `rocks` loop. We want it to be just after that loop. So the `if` statement to check the position of the rocket should be at the same
indentation as the `for` loop over the `rocks`.

OK, so now we have a `score` variable and it increases each time the rocket gets to the top of the game. However, the player has no
way of seeing the score! We need to add some code to show the score on the screen. We need to use another Turtle to add text to the screen.
The following creates a turtle object in a corner of the screen, can you tell which corner it will be? The code hides the turtle because
we do not want to see the turtle itself, we just want to see the text that it is going to write:

```python
score_turtle = Turtle()
score_turtle.goto(190, -170)
score_turtle.hideturtle()
score_turtle.color("white")
```

Finally, we want to get the `score_turtle` to write the score to the screen. Put the following line of code in your main loop:

```python
  update_scores()
```

Again, be careful regarding indentation, and position this code after the score has been increased. Now let's write some code to write the 
score to the screen, put this function definition in the "Scores" section of the code **after** the `score_turtle` has been created:

```python
def update_scores():
  score_turtle.clear()    # delete any current text
  score_msg = XXXX 
  score_turtle.write(score_msg, align="right")
```

What would you put in place for the score text, one choice would be:

```python
  score_msg = "Score: " + str(score)
```

If all is correct, then you should now have a bit of text when the game is started showing the score in the bottom-right corner.
The score should increase if the rocket gets to the end.