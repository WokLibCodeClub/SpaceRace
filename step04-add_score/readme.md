# Step 4 - Adding a score to the game

## The `score` variable

Up to now, we have a rocket, some asteroids, and the rocket can be hit by the asteroids and be sent to the start.
Let's add some code to allow the game to keep track of the score, where the player gets one point if they make it
to the top of the screen.

In the ***=== Scores & Lives ===*** section of the starter code, can you create a variable called `score` and initialise it? What number
should you start a score at? You just need one simple line of code to do this.

<details><summary>Show solution</summary>

```python
score = 0
```

Make sure this line is not indented.

</details>

Now we need the score to increase if the rocket gets to the top edge of the screen. Where do you think we'll need to put the
code for checking if the rocket got to the top of the screen? This is something we need to do not just once, but over and over again. There's a bit of the code that I previously mentioned is always
cycling and checking things... it is the *main loop*. So, we need to add this check at the end of the main `while playing:` loop to see if the rocket has made it to
the top. But how could we determine if the rocket *is* at the top?

We know the size of the screen, it is 400 x 400 pixels, so the y-axis runs from -200 to +200. Therefore, if we can get the y-coordinate of the rocket
then we can check if it is at the top. The following code shows how to check the y-coordinate and compare against the maximum y-coordinate on the screen.
See if you can complete the part labelled TODO in the code:

```python
  if rocket.ycor() > YMAX:
    reset_rocket()
    # TODO Add code to increase the score variable by 1
```

<details><summary>Show solution</summary>

```python
  if rocket.ycor() > YMAX:
    reset_rocket()
    score = score + 1  # add one to the score
```
</details>

Be careful about the indentation here. We do not need to check the position of the rocket everytime we move a rock so we do not want this bit of code
to be inside the `for rock in rocks:` loop. We want it to be *just after* that loop. So the `if` statement to check the position of the rocket should be at the same
indentation as the `for` of the `for rock in rocks:` loop.

OK, so now we have a `score` variable and it increases each time the rocket gets to the top of the screen. However, the player has no
way of seeing the score! We need to add some code to show the score on the screen. We need to use another Turtle to add text to the screen.
The following code creates a turtle object and places it in a corner of the screen. Can you tell which corner it will be? The code hides the turtle because
we do not want to see the turtle itself, we just want to see the text that it is going to write:

***Put the bit of code which sets up this turtle in the `=== Scores & Lives ===` section.***

```python
score_turtle = Turtle()
score_turtle.goto(190, -170)
score_turtle.hideturtle()
score_turtle.color("white")
```

Finally, we want to get the `score_turtle` to write the score to the screen. Put the following line of code ***inside the main `while playing:` loop*** just under the line where you increased
the score:

```python
  update_score()
```

Again, be careful regarding indentation, and position this code after the score has been increased. Again, we've referred to a new function before we've written it! So, now let's write some code to write the 
score to the screen. Put this function definition in the ***`=== Scores & Lives ===` section*** of the code after the `score_turtle` has been created:

```python
def update_score():
  score_turtle.clear()    # delete any current text
  score_msg = XXXX 
  score_turtle.write(score_msg, align="right")
```

`score_msg` is a *text* variable and contains the text that the `score_turtle` will write on the screen. What would you put in place of XXXX? 

<details><summary>Show suggestion</summary>

One choice would be:

```python
  score_msg = "Score: " + str(score)
```

This will write the text **Score: ** and follow it with the value of the variable `score`. But notice, the variable `score` is an integer variable, so if we want to add it to a text variable using the `+` sign we need to convert it to a text string first.

</details>

Lastly, call function `update_score` just after defining it so the score is written to the screen before the main loop starts. This means add the code:

```python
update_score()
```

just before the start of the ***`=== Win or lose ===`*** section of the code.

If all is correct, then you should now see a bit of text when the game is started showing the score in the bottom-right corner.
The score should increase if the rocket gets to the top edge.

[Click here to go to step 5 to add a life limit.](../step05-add_lives/readme.md)

[Back to Step 3](../step03-add_collisions/readme.md)
