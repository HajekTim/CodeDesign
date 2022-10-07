# importieren benötigter Module

import random
import turtle

# setup der beiden Spieler
# Turtle ist der wie ein Stift, wenn penup dann malt er Stift nicht wenn pendown dann schon
player_one = turtle.Turtle()
player_one.speed(10)
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

# male die beiden Ziele
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

wuerfel = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if player_one.pos() >= (300, 100):
        print("Spieler 1 gewinnt!")
        break
    elif player_two.pos() >= (300, -100):
        print("Spieler 2 gewinnt")
        break
    else:
        player_one_turn = input("Spieler 1: Drücke 'Enter' um zu würfeln")
        die_outcome = random.choice(wuerfel)
        print("Spieler 1 würfelt: ", die_outcome)
        print(f"Du gehst {20 * die_outcome} Schritte zum Ziel!")
        player_one.fd(20 * die_outcome)
        player_two_turn = input("Spieler 2: Drücke 'Enter' um zu würfeln")
        die_outcome = random.choice(wuerfel)
        print("Spieler 1 würfelt: ", die_outcome)
        print(f"Du gehst {20 * die_outcome} Schritte zum Ziel!")
        player_two.fd(20 * die_outcome)
