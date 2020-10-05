# Creating the rocks (asteroids)

## Creating a single rock

Next we need to create the asteroids which the player has to avoid.
There will be many asteroids so the code to create the asteroid will be needed many times.
One way to re-use the same bit of code multiple times is to put it in a function.
Two functions were defined in step01 for moving the rocket. As a reminder, the keyword `def`
is used to define a function. Can you write a function with the name `create_rock` which creates
a Turtle object, tells it to use the `asteroid.png` image and to take the pen up. The solution is below.

<details><summary>Show code</summary>

```python
def create_rock():
  rock = Turtle()
  rock.shape("asteroid.png")
  rock.penup()
```
</details>

In the game, there will be some asteroids travelling from right-to-left and some asteroids
travelling from left-to-right. We can modify the `create_rock` function such that it takes an option
which instructs the rock to travel left or travel right. We can do this by adding a function parameter
called `direction` in the parentheses:

```python
def create_rock(direction):
  rock = Turtle()
  rock.shape("asteroid.png")
  rock.penup()
  # This adds the direction parameter to the turtle object
  rock.direction = direction
```

As with the rocket, we need to give each asteroid a heading. In step01, an orientation plot showed the values needed for various directions. Can you remember the values required for left and right? Let's
write a function that can put the asteroid in a starting position and set its heading:

```python
def reset_rock(rock):
  if rock.direction == "right":
    # Start rock at position off the left hand side of screen and tell it to travel right
  elif rock.direction == "left":
    # Start rock at position off the right hand side of screen and tell it to travel left
```

That function takes a rock as a parameter and it checks if the direction of the rock is set to
`"right"` or `"left"`. At the moment I have put a comment in the code to describe the logic
that needs to be completed. The following code block shows the completed function:

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
visible viewing area, this means that when they start travelling they will move into the visible
area and eventually go off the other end of the visible area.

We need to call `reset_rock` on every rock that we create in `create_rock`. Do you know where you will need to put the call to `reset_rock`? It should be put at the bottom, the important bit is that `reset_rock` comes after setting the `direction`: 

```python
def create_rock(direction):
  rock = Turtle()
  rock.shape("asteroid.png")
  rock.penup()
  rock.direction = direction
  reset_rock(rock)

Currently, if we call this function, it will create the rock, set the position and heading,
but do nothing else with it.
When the function gets to the end, the `rock` object will no longer be accessible and will eventually destroyed. In order to keep/store the rock after the function finishes, the rock is returned from the
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

So now we can create a rock by writing the following code:

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

After this code has executed, the `list` should contain 30 rock objects.
The rocket is controlled by the user pressing keys, the asteroids must be moved by the code itself.
That is the final step to the asteroids.

## Set the asteroids in motion

It's time to modify the "Main loop" section of the starter code. The rocks need to be moved as
part of the main loop. In order to move all the rocks, the code must loop over each rock. Can you think of something in python for looping? It is the `for` loop again, the `for` loop can be used to loop
(iterate) over the rocks:

```python
for rock in rocks:
  move_rock(rock)
```

The code above assumes there is a function called `move_rock` which takes a rock as the parameter.
So let's write the `move_rock` function. Here is some incomplete code again, trying filling in the gaps:

```python
def move_rock(rock):
  # Check if rock is going off the edge and reset it if it is.
  xcoord = rock.xcor()
  # If rock goes off the left of the screen then reset
  if rock.direction == "left" and xcoord < XXX:
    reset_rock(rock)
  # If rock goes off the right of the screen then reset
  if rock.direction == "right" and XXX > XMAX:
    reset_rock(rock)
  # Move the rock forward
  rock.XXX(1.5)
```

<details><summary>Click here to see the solution</summary>
```python
def move_rock(rock):
  # Check if rock is going off the edge and reset it if it is.
  xcoord = rock.xcor()
  # If rock goes off the left of the screen then reset
  if rock.direction == "left" and xcoord < XMIN:
    reset_rock(rock)
  # If rock goes off the right of the screen then reset
  if rock.direction == "right" and xcoord > XMAX:
    reset_rock(rock)
  # Move the rock forward
  rock.forward(1.5)
```

 This function takes care of moving the rocks left and right (using rock.forward),
 but it is also responsible for resetting the rocks once they get off the end of the screen.
