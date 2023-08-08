mu=""
score=0
ans1="football"
print("what is brazilian's favorite sport ?")
mu=input()
import turtle
m=turtle.Turtle()
if mu==ans1:
    m.speed(1)
    m.left(150)
    m.forward(100)
    m.back(100)
    m.right(90)
    m.forward(200)
    score=score+1
    
else:
    m.left(45)
    m.fd(150)
    m.bk(300)
    m.fd(150)
    m.right(90)
    m.fd(150)
    m.bk(300)
    m.fd(150)
print("votre score est",score)
print("voulez vous continuer ? o/n")
mu=input()
if mu=="o":
    print("what is the last winner of ballon d'or ?")
    print("1/benzema")
    print("2/ronaldo")
    print("3/messi")
    mu=input()
    if mu=="benzema":
        score==score+2
        print("votre final score est",score,"merci pour votre partcipation")
from random import*
print("veuiller essayer un autre jeux ? o/n")
mu=input()
if mu=="o":
    print("deviner le nombre qui est entre 0 et 10")
    x=randint(1,10)
    mu=int(input("entrer le nombre"))
    if mu==x:
        print("bravo vous avez deviner le nombre")
    else:
        print("desole vous avez pas deviner le nombre")
        print("vous voulez voir c'est quoi le nombre ? o/n")
    mu=input()
    if mu=="o":
        print("le nombre a desviner est",x,"merci de vous participer")
        print("fin de jeux ")
    
 