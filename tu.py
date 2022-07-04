import pygame
import turtle as t

a = input("시작ㄱ:")

scr = t.screen()
scr.setup(800, 480)
scr.bgcolor('orange')
scr.update()

playing = False

from turtle import *
speed(150)
penup()
goto(-200, 140)

for step in range(22):
        color('white')
        write(step, align='center')
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)

from random import randint

def start():
    global playing
    if playing == False:
        playing = True
        play()

def play():
    global playing
    ada = Turtle()
    ada.color('red')
    ada.shape('turtle')
    ada.penup()
    ada.goto(-210, 100)
    ada.pendown()
    bob = Turtle()
    bob.color('blue')
    bob.shape('turtle')
    bob.penup()
    bob.goto(-210, 70)
    bob.pendown()
    ana = Turtle()
    ana.color('yellow')
    ana.shape('turtle')
    ana.penup()
    ana.goto(-210, 50)
    ana.pendown()
    cus = Turtle()
    cus.color('green')
    cus.shape('turtle')
    cus.penup()
    cus.goto(-210, 30)
    cus.pendown()
    for turn in range(140):
        ada.forward(randint(1,5))
        bob.forward(randint(1,5))
        ana.forward(randint(1,5))
        cus.forward(randint(1,5))
    if playing:
        t.ontimer(play, 100)
        ada.ht()
        ana.ht()
        bob.ht()
        cus.ht()
        ada.clear()
        ana.clear()
        bob.clear()

        cus.clear()

def message(m1,m2):

    t.goto(0, 180)
    t.write(m1, False, "center", ("", -40))
    t.goto(-10, -120)
    t.write(m2, False, "center", ("", 20))
    t.home


title("Turtle Race game")
onkeypress(start, "space")

listen()
message("Turtle Race game", "[space]")