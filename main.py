import turtle as t
t.bgcolor("black")
t.pensize(2)
t.speed(10)
for i in range(6):
  for color in ('red','magenta','blue','cyan','green','orange','yellow'):
    t.color(color)
    t.circle(100)
    t.left(10)
  t.hideturtle()