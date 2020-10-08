# Adding lives to the game

So far you have coded up a game with a rocket and asteroids, and there
is a score that increases each time the rocket gets to the end. However, this will go on forever! The game should
have an end. We will give the player 3 lives before it is game over.

In the "Scores & Lives" section of the code, just under the code for setting up the `score_turtle`,  create a `lives`
variable and set it to 3.

<details><summary>Show solution</summary>

```python
lives = 3
```
</details>

Now, copy and paste the code for setting up the `score_turtle` just below your new variable. In the pasted code, replace
the word `score_turtle` with `lives_turtle`. Then change the y-position of the `goto` such that the `lives_turtle` goes
20 units lower than the `score_turtle`. Check your code against the solution below:


<details><summary>Show solution</summary>

```python
lives_turtle = Turtle()
lives_turtle.goto(190, -190)
lives_turtle.hideturtle()
lives_turtle.color("white")
```
</details>

After those changes, we have a `lives` variable to keep track of how many lives the player has, and we have a
`lives_turtle` to write the number to the screen. Now we need to modify the code in the main loop to decrease the
number of lives when the rocket collides with an asteroid. Take a look at the main loop and see if you can find 
where would be a good place to decrease the number of lives? Is there somewhere that already checks for a collision
with a rock? If you said within the `if collides_with_rocket(rock)` block then you are right! Add in a line of
code so it decreases the `lives` variable by 1 if the rocket collides with a rock:

<details><summary>Show solution</summary>

```python
    if collides_with_rocket(rock):
      reset_rocket()
      lives = lives - 1		  # This is the new line
```
</details>

For the `score` variable, we have a `update_score` function to write the `score` to the screen. We need a very similar
function but for the `lives` variable. Try copying and pasting the `update_score` function and calling it `update_lives`.
What do you need to change in the function in order for it to use the `lives_turtle` and also to write text to the screen
that tells the users how many "Lives" they have left. Solution below:

<details><summary>Show solution</summary>

```python
def update_lives():
  lives_turtle.clear()
  lives_turtle.write("Lives: " + str(lives), align="right")
```
</details>

Now call the function after it is defined in order to write the number of lives to the screen before the start of the main loop:

```python
update_lives()
```

The score shown on the screen should now decrease each time the rocket is hit. However, does the game end at 0!? No, it does not,
we need to add more code to finish the game!