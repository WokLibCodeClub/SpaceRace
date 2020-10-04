# Creating the rocket

The first thing we will do is create a rocket which the player will control.

To create the rocket we create a Turtle object and instruct it to use the `rocket.png` image:

```python
rocket = Turtle()
rocket.shape("rocket.png")
```

The turtle library can be used to draw pictures by moving the turtle objects, however, we don't want to draw anything so we tell the turtle to lift the (virtual) pen off the (virtual) paper:

```python
rocket.penup()
```

Now we want to put the rocket at the starting position, the starter code sets the screen size to 400 x 400 pixels.
This means both the x-axis and y-axis start at -200 and finish at +200. We want the rocket to start at the bottom of the y-axis and the middle of the x-axis.
Can you think what those coodinates should be, click "Show code" to see how we move the rocket to the coordinates:

<details><summary>Show code</summary>
  
```python
rocket.goto(0,-190)
```
</details>

Each turtle object has a direction it is facing, the default direction system in turtle looks like this:

![turtle orientation](turtle-orientation.png "Turtle orientation")

0 degress is right, 90 degrees is up, 180 degrees is left and 270 degrees is down.
We want the rocket to be pointing up, the direction of the turtle can be set using the `setheading` function, have a think how the code for that would look
and what number of degrees you would use for the heading.
Check the following code to see if you were right:

<details><summary>Show code</summary>
  
```python
rocket.setheading(90)
```
</details>

Now let's make it possible for the player to move the rocket.
To do this we need to define functions to move the rocket. Here is how to define the function for moving the rocket forward:

```python
def move_rocket_up():
  rocket.forward(5)
```

If we were to call this function like this:

```python
move_rocket_up()
```

then the rocket would move forward by 5 units. There is a function called `back` on the rocket, could you write a function for moving the rocket down.
Check the code below:

<details><summary>Show code</summary>

```python
def move_rocket_down():
  rocket.back(5)
```
</details>

Now we make use of the turtle module to connect these functions to the keyboard arrow keys, referred to with `"up"` and `"down"`:

```python
screen.onkey(move_rocket_up, "up")
screen.onkey(move_rocket_down, "down")
```

That means when the up arrow key is pressed on the keyboard, it will call `move_rocket_up`, when the down arrow key is pressed, it will call `move_rocket_down`.