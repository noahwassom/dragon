import turtle
t = turtle.Turtle()
s = turtle.Screen()
d = 0
p = 0

t.forward(220)
t.right(90)
t.forward(100)
t.right(90)
t.forward(220)
t.right(90)
t.forward(100)
t.right(180)
t.forward(100)
t.left(90)

while d<4:

  t.forward(50)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(30)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(30)
  d=d+1

t.forward(20)
t.left(90)
t.forward(100)
t.right(90)
t.forward(40)
t.left(90)
t.forward(80)
t.left(90)
t.forward(90)
t.left(90)
t.forward(80)
t.left(90)
t.forward(90)

t.left(180)
t.forward(260)
t.left(90)
t.forward(30)
t.right(90)
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.right(90)

while p<4:
  t.left(30)
  t.forward(60)
  t.right(120)
  t.forward(40)
  t.right(120)
  t.forward(40)
  p=p+1


s.exitonclick()
t.color("black", "yellow")
