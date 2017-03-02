print "Hello Pangea!"

from turtle import *

color('red', 'yellow')

begin_fill()

v = 0

while True:
   
    forward(200)
    
    left(90)

    v = v + 1

    if (v) == 4 : break

end_fill()
done()
