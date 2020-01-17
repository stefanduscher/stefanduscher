# Programm:     Uhrdarstellung mit Turtle
#
# Autor:        Stefan Duscher
#
# Datum:        09.06.2019
#
# ----------------------------------------


# Einbindung der Bibliotheken
import turtle as trt
from datetime import datetime


def jump(distanz, winkel=0):
    # Sprungfunktion für die Turtle; sie hebt den Stift, läuft die
    # übergebene Entfernung und senkt den Stift wieder
    trt.penup()             # Stift anheben
    trt.forward(distanz)    # Laufen
    trt.pendown()           # Stift absenken



def zeiger(laenge, spitze):
    # Diese Funktion zeichnet einen Pfeil
    trt.fd(laenge*1.15)
    trt.rt(90)
    trt.fd(spitze/2.0)
    trt.lt(120)
    trt.fd(spitze)
    trt.lt(120)
    trt.fd(spitze)
    trt.lt(120)
    trt.fd(spitze/2.0)


def zeichne_vollen_zeiger(name, laenge, spitze):
    # Diese Funktion zeichnet einen gefüllten Zeiger
    trt.reset()
    jump(-laenge*0.15)
    trt.begin_poly()
    zeiger(laenge, spitze)
    trt.end_poly()
    hand_form = trt.get_poly()
    trt.register_shape(name, hand_form)

def ziffernblatt(radius):
    # Diese Funktion zeichnet das Ziffernblatt
    trt.reset()
    trt.pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            trt.fd(25)
            jump(-radius-25)
        else:
            trt.dot(3)
            jump(-radius)
        trt.rt(6)

def setup():
    global sekundenzeiger, minutenzeiger, stundenzeiger, writer
    trt.mode("logo")
    zeichne_vollen_zeiger("sekundenzeiger", 125, 25)
    zeichne_vollen_zeiger("minutenzeiger",  130, 25)
    zeichne_vollen_zeiger("stundenzeiger", 90, 25)
    ziffernblatt(160)
    sekundenzeiger = trt.Turtle()
    sekundenzeiger.shape("sekundenzeiger")
    sekundenzeiger.color("gray20", "gray80")
    minutenzeiger = trt.Turtle()
    minutenzeiger.shape("minutenzeiger")
    minutenzeiger.color("blue1", "red1")
    stundenzeiger = trt.Turtle()
    stundenzeiger.shape("stundenzeiger")
    stundenzeiger.color("blue3", "red3")
    for hand in sekundenzeiger, minutenzeiger, stundenzeiger:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    trt.ht()
    writer = trt.Turtle()
    writer.ht()
    writer.pu()
    writer.bk(85)

def wochentag(t):
    wochentag = ["Montag", "Dienstag", "Mittwoch",
        "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    return wochentag[t.weekday()]

def datum(z):
    monat = ["Jan.", "Feb.", "Mar.", "Apr.", "Mai", "Juni",
             "July", "Aug.", "Sep.", "Okt.", "Nov.", "Dez."]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j) # gibt String und zwei Zahlen zurück


def tick():
    t = datetime.today()
    sekunde = t.second + t.microsecond*0.000001
    minute = t.minute + sekunde/60.0
    stunde = t.hour + minute/60.0
  
    trt.tracer(False)
    writer.clear()
    writer.home()
    writer.forward(65)
    writer.write(wochentag(t),
                     align="center", font=("Courier", 16, "bold"))
    writer.back(150)
    writer.write(datum(t),
                     align="center", font=("Courier", 14, "bold"))
    writer.forward(85)
    trt.tracer(True)
    sekundenzeiger.setheading(6*sekunde)
    minutenzeiger.setheading(6*minute)
    stundenzeiger.setheading(30*stunde)
    trt.tracer(True)
    trt.ontimer(tick, 100)
    

def main():
    trt.tracer(False)
    setup()
    trt.tracer(True)
    tick()



# Hauptprogramm

trt.mode("logo")
main()
trt.mainloop()



