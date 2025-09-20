from random import randrange, choice
from turtle import *
from freegames import square, vector
import time
#el random es necesario para los colores
import random

#opciones de color para la fruta y la serpiente
body_colors = ('black', 'brown', 'orange', 'green', 'violet')
food = vector(0, 0)
snake = [vector(10, 0)]

#añadimos la fruta extra al juego
super_food = vector(1000, 1000)
aim = vector(0, -10)
start_time = time.time()

#Color final aleatorio de la fruta y la serpiente (será diferente cada que se empieza una partida)
snake_color = random.choice(body_colors)
fruit_color = random.choice(body_colors)

#velocidad inicial de la serpiente
snake_speed = 150

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

#función que hace que la fruta se mueva una casilla cada cierto tiempo
def move_food():
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    step = choice(directions)
    new_food = food.copy()
    new_food.move(step)

    if inside(new_food):
        food.move(step)
    ontimer(move_food, 5000)

def spawn_super_food():
    #Hace aparecer la súper comida en un lugar aleatorio.
    super_food.x = randrange(-15, 15) * 10
    super_food.y = randrange(-15, 15) * 10
    ontimer(despawn_super_food, 4000) 
    ontimer(spawn_super_food, 12000)  

def despawn_super_food():
    #Esconde la súper comida (la manda fuera del tablero).
    super_food.x = 1000
    super_food.y = 1000

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    global snake_speed
    head = snake[-1].copy()
    head.move(aim)
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        show_stats()
        return

# Definir que es lo que ocurre cuando la serpiente choca con un obstáculo (el juego termina)
    if not inside (head) or head in snake or head in obstacles:
        square(head.x, head.y, 9, 'red')
        update()
        show_stats()
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
        #Codigo que al comer una fruta aumenta la velocidad de la serpiente
        if snake_speed > 50: #minimo de velocidad
            snake_speed -= 5
            print("Nueva velocidad", snake_speed, "ms")
                
    elif head == super_food:
        print('Snake comió SUPER comida! Largo:', len(snake) + 2)
        despawn_super_food()  
        snake.append(snake[-1].copy()) 
        if snake_speed > 50: #minimo de velocidad
                snake_speed -= 10
                print("Nueva velocidad", snake_speed, "ms")

    else:
        snake.pop(0)

    clear()

    #cambio en el codigo para que el color aleatorio sea uniforme durante toda la partida
    for body in snake:
        square(body.x, body.y, 9, snake_color)
    
    square(food.x, food.y, 9, fruit_color)

    #al ser un objeto especial su color será uno en especifo
    square(super_food.x, super_food.y, 9, 'yellow')

    #definir el color del obstaculo (un color definido)
    for obs in obstacles:
        square(obs.x, obs.y, 9, 'blue')
    update()
    #velocidad final tras comer una fruta
    ontimer(move, snake_speed) 
    
#codigo que Muestra las estadísticas del juego al final.
def show_stats():
    #codigo que cuenta el tiempo total de juego
    game_time = time.time() - start_time
    minutes = int(game_time // 60)
    seconds = int(game_time % 60)
    growth = len(snake) - 1

    #Texto monstrado en la pantalla cuando termina el juego
    clear()
    penup()
    goto(0, 50)
    color('red')
    write("¡Juego Terminado!", align="center", font=("Arial", 16, "bold"))
    
    goto(0, 20)
    color('black')
    write(f"Tiempo: {minutes} min {seconds} seg", align="center", font=("Arial", 12, "normal"))

    #Codigo para que el juego no diga "1 puntos" cuando el puntaje sea igual a 1
    goto(0, -10)
    if (growth == 1):
        write(f"Puntaje final: {growth} punto", align="center", font=("Arial", 12, "normal"))
    else:
        write(f"Puntaje final: {growth} puntos", align="center", font=("Arial", 12, "normal"))
    
    goto(0, -40)
    write(f"Longitud final: {len(snake)}", align="center", font=("Arial", 12, "normal"))
    
    update()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
spawn_super_food()
move_food()
move()
done()

