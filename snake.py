
from random import randrange
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Definir la variable de los obstaculos
obstacles = []

# for que definen la posición de los obstaculos en el mapa
for i in range (10, 80, 10):
    obstacles.append(vector(-150, i))
for i in range (-70, 0, 10):
    obstacles.append(vector(100, i))
for i in range (-150, -70, 10):
    obstacles.append(vector(i, -100))
for i in range (-70, 0, 10):
    obstacles.append(vector(i, 50))
    
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

# Definir que es lo que ocurre cuando la serpiente choca con un obstáculo (el juego termina)
    if not inside (head) or head in snake or head in obstacles:
        square(head.x, head.y, 9, 'red')
        update()
        return
    
    snake.append(head)

   #Cambio en la función para evitar que "food" aparezca en los obstaculos
    if head == food:
        print('Snake:', len(snake))
        while True:
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
            if food not in obstacles and food not in snake:
                break
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')

    #definir el color del obstaculo
    for obs in obstacles:
        square(obs.x, obs.y, 9, 'blue')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()



