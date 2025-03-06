# Step 2 - Creating the rocks (asteroids)

## Creating a single rock

***ALMOST All the code in this step should go in the part of the code headed `=== Rocks ===` immediately after 'while playing:'***

Next we need to create the asteroids which the player has to avoid.
There will be many asteroids so the code to create the asteroid will be needed many times.
One way to re-use the same bit of code multiple times is to put it in a function.
We already defined two functions step 1 for moving the rocket. As a reminder, the keyword ```def```
is used to define a function. Can you write a function with the name `create_rock` which creates
a Turtle object, tells it to use the `asteroid.png` image as its shape, and lifts the pen up? The solution is below.

<details><summary>Show code</summary>

```python
def create_rock():
  rock = Turtle()
  rock.shape("asteroid.png")
  rock.penup()
```
</details>

In the game, there will be some asteroids travelling from right-to-left and some asteroids
travelling from left-to-right. We can modify the `create_rock` function so that it takes in information
which instructs the rock to travel either left or right. We can do this by adding a function *parameter*
called `direction` in the parentheses. Here is the revised function:

```python
def create_rock(direction): # Notice the parameter inside the brackets
  rock = Turtle()
  rock.shape("asteroid.png")
  rock.penup()
  # Add a direction parameter to the turtle object and set it to the direction received as a parameter
  rock.direction = direction
```

As with the rocket, we need to give each asteroid a heading. In step 1, there was a diagram which showed the angle values needed for various heading directions. Can you remember the values required for left and right? Let's write a new function that can put the asteroid in a suitable starting position and set its heading:

```python
def reset_rock(rock):
  if rock.direction == "right":
    # Start rock at position off the left hand side of screen and tell it to travel right
  elif rock.direction == "left":
    # Start rock at position off the right hand side of screen and tell it to travel left
```

This function takes ```rock``` as a parameter and it checks if the direction of the rock is set to
`"right"` or `"left"`. The comments in the code  describe the logic that needs to be completed. The following code block shows the completed function:

```python
def reset_rock(rock):
  if rock.direction == "right":
    rock.setheading(0)
    random_pos = (randint(XMIN - 1.25*WIDTH, XMIN), randint(-150,180))
    rock.goto(random_pos)
  elif rock.direction == "left":
    rock.setheading(180)
    random_pos = (randint(XMAX, XMAX + 1.25*WIDTH), randint(-150,180))
    rock.goto(random_pos)
```

This generates random starting positions for the asteroids. These positions are actually off the
visible viewing area (off the screen to the left if the rock is travelling "right", and off to the right if the rock is travelling "left"). This means that when the rocks start travelling they will move into the visible area and eventually go off the other side of the visible area.

We need to call function ```reset_rock``` for every rock that we create with function ```create_rock```. Do you know where you will need to put the call to `reset_rock`? It should be put at the bottom of function ```create_rock```. **Note:** it's important that `reset_rock` is called *after* setting the `direction`: 

```python
def create_rock(direction):
  rock = Turtle()
  rock.shape("asteroid.png")
  rock.penup()
  rock.direction = direction
  reset_rock(rock)
```

Currently, if we call this function, it will create a rock, set the position and heading, but do nothing else with it.
When the function gets to the end, the `rock` object will no longer be accessible and will eventually be destroyed. In order to keep/store/use the rock after the function finishes, the rock is *returned* from the
function by using the `return` keyword:

```python
def create_rock(direction):
  rock = Turtle()
  rock.shape("asteroid.png")
  rock.penup()
  rock.direction = direction
  reset_rock(rock)
  return rock     # return the rock to the function caller
```

So now we can create a rock by writing one or other of the following bits of code:

```python
rock = create_rock("left")
```

or

```python
rock = create_rock("right")
```

However, that will give us just one rock, and we want lots of rocks!

## Creating multiple rocks

In order to create multiple rocks we are going to use a couple of `for` loops.
Some incomplete code is below, the missing parts are indicated with XXX.
See if you can fill in the missing parts:

```python
# List to hold all rocks
rocks = []
number_of_left_rocks = 15
number_of_right_rocks = 15

# Create rocks going right
for _ in range(XXX):
  rock = create_rock("right")
  rocks.append(XXX)

# Create rocks going left
for _ in range(number_of_left_rocks):
  XXX = create_rock("XXX")
  XXX.append(rock)
```

<details><summary>Click here to see the solution</summary>

```python
# List to hold all rocks
rocks = []
number_of_left_rocks = 15
number_of_right_rocks = 15

# Create rocks going right
for _ in range(number_of_right_rocks):
  rock = create_rock("right")
  rocks.append(rock)

# Create rocks going left
for _ in range(number_of_left_rocks):
  rock = create_rock("left")
  rocks.append(rock)
```
</details>

After this code has executed, the `rocks` list should contain 30 rock objects.

Although the rocket is controlled by the user pressing keys, the asteroids must be moved by the code itself.
That is the final step of the asteroids step.

## Setting the asteroids in motion

***The next bit of code should go in the part of the project headed `=== Main loop ===`.*** 

It's time to modify the "Main loop" section of the starter code. The rocks need to be moved as part of the main loop because in order to move *all* the rocks, the code must loop over each rock and this is something that needs to be done over and over again. We will loop over all the rocks using a `for` loop again:

```python
for rock in rocks:
  move_rock(rock)
```

The code above assumes there is a function called `move_rock` which takes a rock as the parameter, but we haven't written this function yet.
So let's write the `move_rock` function. 

***Put this function in the `=== Rocks ===` section.***

Here is some incomplete code again, trying filling in the gaps:

```python
def move_rock(rock):
  # Check if rock is going off the edge and reset it if it is.
  xcoord = rock.xcor()
  # If rock goes off the left of the screen then reset it by calling the reset_rock function
  if rock.direction == "left" and xcoord < XXX:
    reset_rock(rock)
  # If rock goes off the right of the screen then reset it
  if rock.direction == "right" and XXX > XMAX:
    reset_rock(rock)
  # If the rock is not going off either edge then move the rock forward
  rock.XXX(1.5)
```

<details><summary>Click here to see the solution</summary>
  
```python
def move_rock(rock):
  # Check if rock is going off the edge and reset it if it is.
  xcoord = rock.xcor()
  # If rock goes off the left of the screen then reset it by calling the reset_rock function
  if rock.direction == "left" and xcoord < XMIN:
    reset_rock(rock)
  # If rock goes off the right of the screen then reset it
  if rock.direction == "right" and xcoord > XMAX:
    reset_rock(rock)
  # If the rock is not going off either edge then move the rock forward
  rock.forward(1.5)
```
</details>

 This function takes care of moving the rocks (either to the left or the right, using `rock.forward`),
 but it is also responsible for resetting the rocks once they get off the edges of the screen.

Once you have completed this step, you should see asteroids flying left and right across the screen.

Don't forget to ***test*** your code.

[Click here to go to step 3 to add collisions between the rocks and the rocket.](../step03-add_collisions/readme.md)

[Back to Step 1](../step01-create_rocket/readme.md)
