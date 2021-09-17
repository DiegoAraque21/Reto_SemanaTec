"""Snake, classic arcade game.

Exercises

LuisFe--->1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
LuisF----->3. How would you move the food?
LuisF---->4. Change the snake to respond to arrow keys.

Extra
Change the color of board



"""

from turtle import *
from random import randrange
from freegames import square, vector

import random as rd
<<<<<<< HEAD
=======
"Change the initial position of food and snake"

"Library to use randint"
import random as rd

"Change the initial position of food and snake"

"Library to use randint"
import random as rd

"Change the initial position of food and snake"

"Library to use randint"
import random as rd
>>>>>>> f4fd5a8d476ee5be40f263ad0d37787a9c4b9f3e

"Change the initial position of food and snake"

a=round(rd.randint(-9,9)*10)
b=round(rd.randint(-9,9)*10)
c=round(rd.randint(-9,9)*10)
d=round(rd.randint(-9,9)*10)
print(a,b,c,d)

food = vector(c, d)
snake = [vector(a, b)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'purple')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
<<<<<<< HEAD
    "Change the speed LuisFe"
    f=len(snake)
    if f<10:
        ontimer(move, 100)
    else:
        ontimer(move,50)
=======
    #The snake can be faster if in the ontimeter the second argument is changed
    #when the number is close to 0 the speed is higher and when it is to far from 0
    #it goes slower. In this case we changed it fromo 100 to 50, and it clearly goes faster
    ontimer(move, 50)

>>>>>>> f4fd5a8d476ee5be40f263ad0d37787a9c4b9f3e
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
<<<<<<< HEAD
"LuisFe 4. Change the snake to respond to arrow keys"
"Right"
onkey(lambda: change(10, 0), 'D')
"Left"
onkey(lambda: change(-10, 0), 'A')
"Up"
onkey(lambda: change(0, 10), 'W')
"Down"
onkey(lambda: change(0, -10), 'S')
=======
"Change control keys form Up, Down, Right and Left to WASD" 
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
>>>>>>> f4fd5a8d476ee5be40f263ad0d37787a9c4b9f3e
move()
done()
