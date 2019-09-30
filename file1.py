from graph import *
import random

c=canvas()
canvasSize(700, 900)
windowSize(1000, 900)
ddx=0

def background(cvetneba,cvetgor,cvetzemli,cvetklumbi):
    global bgrnd,sol,lun
    penColor(cvetneba)
    brushColor(cvetneba)
    bgrnd=rectangle(0,0,700,300)
    penColor(cvetgor)
    brushColor(cvetgor)
    polygon(((0,100),(50,50),(100,110),(200,55),(400,200),(500,75),(600,100),(700,50),(700,600),(0,600),(0,100)))
    penColor(cvetzemli)
    brushColor(cvetzemli)
    polygon(((0,500),(300,500),(300,550),(700,550),(700,900),(0,900),(0,500)))
    penColor(cvetklumbi)
    brushColor(cvetklumbi)
    circle(570,670,100)
    penColor('yellow')
    brushColor('yellow')
    sol = rectangle(0, 0, 50, 50)
    penColor('white')
    brushColor('white')
    lun = rectangle(-50, 0, 0, 50)

def body(cvettela,cvetglas):
    global glas1,glas2
    c.create_oval(50,600,250,700,fill=cvettela,outline=cvettela)
    c.create_oval(200,520,250,650,fill=cvettela,outline=cvettela)
    c.create_oval(200,500,280,540,fill=cvettela,outline=cvettela)
    glas1=c.create_oval(220,505,250,530,fill=cvetglas,outline=cvetglas)
    glas2=c.create_oval(235,510,245,525,fill='black',outline='black')
    c.create_oval(225,507,240,515,fill=cvettela,outline=cvettela)
    c.create_oval(195,475,225,515,fill=cvettela,outline=cvettela)

    c.create_oval(55,650,85,730,fill=cvettela,outline=cvettela)
    c.create_oval(55,720,85,780,fill=cvettela,outline=cvettela)
    c.create_oval(55,775,95,795,fill=cvettela,outline=cvettela)

    c.create_oval(95,660,125,740,fill=cvettela,outline=cvettela)
    c.create_oval(95,730,125,790,fill=cvettela,outline=cvettela)
    c.create_oval(95,785,135,805,fill=cvettela,outline=cvettela)

    c.create_oval(190,650,220,730,fill=cvettela,outline=cvettela)
    c.create_oval(190,720,220,780,fill=cvettela,outline=cvettela)
    c.create_oval(190,775,230,795,fill=cvettela,outline=cvettela)

    c.create_oval(225,660,255,740,fill=cvettela,outline=cvettela)
    c.create_oval(225,730,255,790,fill=cvettela,outline=cvettela)
    c.create_oval(225,785,265,805,fill=cvettela,outline=cvettela)

def klumba():
    global b1,b2,b3,b4,b5,b6,b7
    x = 540
    y = 620
    b1 = (c.create_oval(x - 10, y - 25, x + 10, y - 10, fill='white', outline='white'),
          c.create_oval(x - 25, y - 10, x - 5, y + 5, fill='white', outline='white'),
          c.create_oval(x + 5, y - 10, x + 25, y + 5, fill='white', outline='white'),
          c.create_oval(x - 10, y + 5, x + 10, y + 20, fill='white', outline='white'),

          c.create_oval(x - 20, y - 20, x, y - 5, fill='white', outline='white'),
          c.create_oval(x, y - 20, x + 20, y - 5, fill='white', outline='white'),
          c.create_oval(x, y, x + 20, y + 15, fill='white', outline='white'),
          c.create_oval(x - 20, y, x, y + 15, fill='white', outline='white'),
          c.create_oval(x - 10, y - 10, x + 10, y + 5, fill='yellow', outline='yellow'))
    x = 605
    y = 620
    b2 = (c.create_oval(x - 10, y - 25, x + 10, y - 10, fill='white', outline='white'),
          c.create_oval(x - 25, y - 10, x - 5, y + 5, fill='white', outline='white'),
          c.create_oval(x + 5, y - 10, x + 25, y + 5, fill='white', outline='white'),
          c.create_oval(x - 10, y + 5, x + 10, y + 20, fill='white', outline='white'),

          c.create_oval(x - 20, y - 20, x, y - 5, fill='white', outline='white'),
          c.create_oval(x, y - 20, x + 20, y - 5, fill='white', outline='white'),
          c.create_oval(x, y, x + 20, y + 15, fill='white', outline='white'),
          c.create_oval(x - 20, y, x, y + 15, fill='white', outline='white'),
          c.create_oval(x - 10, y - 10, x + 10, y + 5, fill='yellow', outline='yellow'))
    x = 630
    y = 670
    b3 = (c.create_oval(x - 10, y - 25, x + 10, y - 10, fill='white', outline='white'),
          c.create_oval(x - 25, y - 10, x - 5, y + 5, fill='white', outline='white'),
          c.create_oval(x + 5, y - 10, x + 25, y + 5, fill='white', outline='white'),
          c.create_oval(x - 10, y + 5, x + 10, y + 20, fill='white', outline='white'),

          c.create_oval(x - 20, y - 20, x, y - 5, fill='white', outline='white'),
          c.create_oval(x, y - 20, x + 20, y - 5, fill='white', outline='white'),
          c.create_oval(x, y, x + 20, y + 15, fill='white', outline='white'),
          c.create_oval(x - 20, y, x, y + 15, fill='white', outline='white'),
          c.create_oval(x - 10, y - 10, x + 10, y + 5, fill='yellow', outline='yellow'))
    x = 510
    y = 670
    b4 = (c.create_oval(x - 10, y - 25, x + 10, y - 10, fill='white', outline='white'),
          c.create_oval(x - 25, y - 10, x - 5, y + 5, fill='white', outline='white'),
          c.create_oval(x + 5, y - 10, x + 25, y + 5, fill='white', outline='white'),
          c.create_oval(x - 10, y + 5, x + 10, y + 20, fill='white', outline='white'),

          c.create_oval(x - 20, y - 20, x, y - 5, fill='white', outline='white'),
          c.create_oval(x, y - 20, x + 20, y - 5, fill='white', outline='white'),
          c.create_oval(x, y, x + 20, y + 15, fill='white', outline='white'),
          c.create_oval(x - 20, y, x, y + 15, fill='white', outline='white'),
          c.create_oval(x - 10, y - 10, x + 10, y + 5, fill='yellow', outline='yellow'))
    x = 570
    y = 670
    b5 = (c.create_oval(x - 10, y - 25, x + 10, y - 10, fill='white', outline='white'),
          c.create_oval(x - 25, y - 10, x - 5, y + 5, fill='white', outline='white'),
          c.create_oval(x + 5, y - 10, x + 25, y + 5, fill='white', outline='white'),
          c.create_oval(x - 10, y + 5, x + 10, y + 20, fill='white', outline='white'),

          c.create_oval(x - 20, y - 20, x, y - 5, fill='white', outline='white'),
          c.create_oval(x, y - 20, x + 20, y - 5, fill='white', outline='white'),
          c.create_oval(x, y, x + 20, y + 15, fill='white', outline='white'),
          c.create_oval(x - 20, y, x, y + 15, fill='white', outline='white'),
          c.create_oval(x - 10, y - 10, x + 10, y + 5, fill='yellow', outline='yellow'))
    x = 540
    y = 720
    b6 = (c.create_oval(x - 10, y - 25, x + 10, y - 10, fill='white', outline='white'),
          c.create_oval(x - 25, y - 10, x - 5, y + 5, fill='white', outline='white'),
          c.create_oval(x + 5, y - 10, x + 25, y + 5, fill='white', outline='white'),
          c.create_oval(x - 10, y + 5, x + 10, y + 20, fill='white', outline='white'),

          c.create_oval(x - 20, y - 20, x, y - 5, fill='white', outline='white'),
          c.create_oval(x, y - 20, x + 20, y - 5, fill='white', outline='white'),
          c.create_oval(x, y, x + 20, y + 15, fill='white', outline='white'),
          c.create_oval(x - 20, y, x, y + 15, fill='white', outline='white'),
          c.create_oval(x - 10, y - 10, x + 10, y + 5, fill='yellow', outline='yellow'))
    x = 605
    y = 720
    b7 = (c.create_oval(x - 10, y - 25, x + 10, y - 10, fill='white', outline='white'),
          c.create_oval(x - 25, y - 10, x - 5, y + 5, fill='white', outline='white'),
          c.create_oval(x + 5, y - 10, x + 25, y + 5, fill='white', outline='white'),
          c.create_oval(x - 10, y + 5, x + 10, y + 20, fill='white', outline='white'),

          c.create_oval(x - 20, y - 20, x, y - 5, fill='white', outline='white'),
          c.create_oval(x, y - 20, x + 20, y - 5, fill='white', outline='white'),
          c.create_oval(x, y, x + 20, y + 15, fill='white', outline='white'),
          c.create_oval(x - 20, y, x, y + 15, fill='white', outline='white'),
          c.create_oval(x - 10, y - 10, x + 10, y + 5, fill='yellow', outline='yellow'))

def sdvig():
    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)
    for i in b1:
        moveObjectBy(i,dx,dy)
    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)
    for i in b2:
        moveObjectBy(i, dx, dy)
    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)
    for i in b3:
        moveObjectBy(i, dx, dy)
    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)
    for i in b4:
        moveObjectBy(i, dx, dy)
    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)
    for i in b5:
        moveObjectBy(i, dx, dy)
    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)
    for i in b6:
        moveObjectBy(i, dx, dy)
    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)
    for i in b7:
        moveObjectBy(i, dx, dy)

def morg2():
    changePenColor(glas1, 'white')
    changeFillColor(glas1, 'white')
    changePenColor(glas2, 'white')
    changeFillColor(glas2, 'white')

def morg1():
    changePenColor(glas2, 'black')
    changeFillColor(glas2, 'black')
    changeFillColor(glas1, 'purple')
    changePenColor(glas1, 'purple')

def solnce():
    global ddx,sol,lun
    ddx+=10
    if ddx>1400:
        ddx=0
    moveObjectTo(sol,ddx,150)

    if ddx>700:
        moveObjectTo(lun, 0 + ddx - 700, 150)
        changeFillColor(bgrnd,"DarkBlue")
    else:
        changeFillColor(bgrnd, "DarkOrange")


background('blue', 'gray', 'green', 'DarkGreen')
body('white', 'purple')
klumba()


onTimer(sdvig,100)
onTimer(morg1,550)
onTimer(morg2,1000)
onTimer(solnce,100)

run()