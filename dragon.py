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
t.forward(20)
t.left(90)
t.forward(70)


t.left(0)
t.forward(30)
t.right(120)
t.forward(30)
t.right(120)
t.forward(30)
t.left(120)
t.forward(30)
t.right(120)
t.forward(30)
t.left(120)
t.forward(30)
t.right(120)
t.forward(30)
t.right(120)
t.forward(90)
t.right(180)
t.forward(100)
t.left(90)
t.forward(30)
t.right(90)



while p<3:
  t.left(-0)
  t.forward(50)
  t.right(-120)
  t.forward(50)
  t.right(-120)
  t.forward(50)
  t.left(120)
  t.forward(50)
  p=p+1

  
  #withcolor:
  
  import turtle
t = turtle.Turtle()
s = turtle.Screen()
d = 0
p = 0

t.color("blue")
t.begin_fill()
t.forward(220)
t.right(90)
t.forward(100)
t.right(90)
t.forward(220)
t.right(90)
t.forward(100)
t.end_fill()
t.right(180)
t.forward(100)
t.left(90)


while d<4:
  t.color("teal")
  t.begin_fill()
  t.forward(50)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(30)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(30)
  t.end_fill()
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

t.begin_fill()
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
t.end_fill()

while p<4:
  t.left(30)
  t.forward(60)
  t.right(120)
  t.forward(40)
  t.right(120)
  t.forward(40)
  p=p+1

s.exitonclick()
