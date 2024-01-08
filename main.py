from turtle import Screen
import time
from snake import Snake
from food import Food
from scorecard import Scorecard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Lifeless Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scorecard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        print('crisp!')

    # Detecting collision with wall
    if snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() > 280 or snake.head.xcor() < -280:
        is_game_on = False
        score.game_over()

    # Detecting collision with tail
    for segments in snake.boxes[1:]:
        if snake.head.distance(segments) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
