import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from tkinter.font import *
from tkinter import messagebox
from random import *
import time


#variable pong :
Largeur = 810
Hauteur = 540

# Les coordonnées de départ de la balle
x0, y0 = 400,270
dx = +8 # Vitesse horizontale
dy = +8  # Vitesse verticale
#coordonnees raquette 1 :
deuy0 = 210
#coordonnees raquette 2 :
troiy0 = 210

joueur1 = 0
joueur2 = 0

#variables devinombre :
nbe = "Nombres d'essais : "
ten = "Tentatives restantes : "
tent = 10
lvl = 1
cmax = 10
n = randint(0, cmax)


#variables morpion :
#la croix commence donc c'est True
clic = True
decompte = 0
vert = True



fenetre = tk.Tk()
fenetre.title("Menu principal")
fenetre.geometry('810x540')

c = Canvas(fenetre, bg="blue", height=540, width=810)
imgmenu = PhotoImage(file =r"Fond Menu.png")
c.create_image(0,0, anchor=NW ,image = imgmenu)
c.place(x=0, y=0)

def fenchoix():
    fenchoix = tk.Toplevel()
    fenchoix.title("Choix du jeu")
    fenchoix.geometry('810x540')

    cchoi = Canvas(fenchoix, height=540, width=810)
    imgchoi = PhotoImage(file =r"Fond CHOIX.png")
    cchoi.create_image(0,0, anchor=NW ,image = imgchoi)
    cchoi.place(x=0, y=0)

    boutonretour2 = PhotoImage(file="Bouton RETOUR.png")
    bm8 = tk.Button(fenchoix, text ="Retour", command = fenchoix.destroy, image=boutonretour2, bg="#FFE1E9", height = 50, width = 140, relief=FLAT)
    bm8.place(x=320, y=400) 
    boutonpong = PhotoImage(file=r"Bouton PONG.png")
    bm5 = tk.Button(fenchoix, text ="Pong",image=boutonpong,command=pong, bg="#FFE1E9", height = 130, width = 130, relief=FLAT)
    bm6 = tk.Button(fenchoix, text ="Morpion", command=morpion, height = 7,bg="#FFE1E9", width = 16, relief=FLAT)
    bm7 = tk.Button(fenchoix, text ="Devi-nombre", command=devinombre, height = 7,bg="#FFE1E9", width = 16, relief=FLAT)
    bm5.place(x=150, y=200) 
    bm6.place(x=350, y=200) 
    bm7.place(x=550, y=200)
    fenchoix.mainloop()
    
def fenregles():
    fenregles = tk.Toplevel()
    fenregles.title("Règles de jeux")
    fenregles.geometry('810x540')

    creg = Canvas(fenregles, height=540, width=810)
    imgregles = PhotoImage(file =r"Fond REGLES.png")
    creg.create_image(0,0, anchor=NW ,image = imgregles)
    creg.place(x=0, y=0)

    boutonretour = PhotoImage(file="Bouton RETOUR.png")
    bm4 = tk.Button(fenregles, text ="Retour", command = fenregles.destroy, image=boutonretour, bg="#FFE1E9", height = 50, width = 140, relief=FLAT)
    bm4.place(x=320, y=400) 
    fenregles.mainloop()

def pong():
    global Largeur, Hauteur, x0, y0, dx, dy, deuy0, troiy0, joueur1, joueur2


    def acceuil():
        saisi=str(e1.get())
        saisi2=str(e2.get())    
        print(saisi, saisi2)
        
        nom()


    
    menu = Tk()
    menu.geometry('470x200')
    menu.title("PONG")


    labl1 = Label(menu, text = "Nom joueur 1 :")
    labl1.pack(padx= 5, pady = 5)

    e1=Entry(menu)
    e1.pack(padx= 0, pady = 5)

    labl2 = Label(menu, text = "Nom joueur 2 :")
    labl2.pack(padx= 5, pady = 5)

    e2=Entry(menu)
    e2.pack(padx= 0, pady = 5)

    buttonOk = Button(menu,text='OK',command=acceuil)
    buttonOk.pack(padx= 5, pady = 5)



    def nom():
        global saisi, saisi2
        saisi=str(e1.get())
        saisi2=str(e2.get())
        if saisi == "" :
            lab1.configure(text="JOUEUR 1 : 0")
        else :
            lab1.configure(text=saisi +  " : 0")
        if saisi2 == "" :
            lab2.configure(text="JOUEUR 2 : 0")
        else :
            lab2.configure(text=saisi2 +  " : 0")
        
    def rejouer():
        global x0,y0,dx,dy,troiy0, deuy0, joueur2, joueur1, saisi, saisi2
        saisi=str(e1.get())
        saisi2=str(e2.get())

        # Les coordonnées de départ de la balle et sa vitesse
        x0, y0 = 400,270
        dx = +8 # Vitesse horizontale
        dy = +8 # Vitesse verticale
        #coordonnees raquette 1 :

        joueur1 = 0
        joueur2 = 0
        
        if saisi == "" :
            lab1.configure(text="JOUEUR 1 : 0")
        else :
            lab1.configure(text=saisi +  " : 0")
        if saisi == "" :
            lab2.configure(text="JOUEUR 2 : 0")
        else :
            lab2.configure(text=saisi2 +  " : 0")
    


        deplacer()

    def commencer():
        deplacer()

    def deplacer():
        global x0,y0,dx,dy,troiy0, deuy0, joueur2, joueur1  
        x0 = x0 + dx # Nouvelle abscisse
        y0 = y0 + dy # Nouvelle ordonnée
        perdu = False

        canvas.coords(balle,x0,y0,x0+20,y0+20) # Déplacement
        #La raquette 1 renvoie la balle
        if x0 < -30 :
            if y0 < deuy0 or y0 > deuy0+100 :
                print("perdu")
                joueur2 = joueur2 + 1
                if saisi2 == "" :
                    lab2.configure(text="JOUEUR 2 : "+str(joueur2))
                else :
                    lab2.configure(text=saisi2 + " : "+str(joueur2))
                perdu = True
                
        if x0 < 35 and y0 > deuy0-2 and y0 < deuy0 + 102 :
            dx = -dx
        #La raquette 2 renvoie la balle
        if x0 > Largeur + 10 :
            if y0 < troiy0 or y0 > troiy0 +100 :
                print("perdu")
                joueur1 = joueur1 + 1
                if saisi == "" :
                    lab1.configure(text="JOUEUR 1: "+str(joueur1))
                else :
                    lab1.configure(text=saisi +  " : "+str(joueur1))
                perdu = True
                
        if x0 > Largeur - 55 and y0 > troiy0-2 and y0 < troiy0+102 :
            dx = -dx
                
                    
        if y0 < 0 or y0 > Hauteur-20:
            dy = -dy # Changement de sens vertical

        
        if joueur1 == 5 :
            print('j1 win')
            tk=Tk()
            tk.title("VAINQUEUR")
            tk.geometry('450x100')
            if saisi == "" :
                lab3 = Label(tk, text="Le JOUEUR 1 a gagné")
                lab3.pack(padx=5,pady=5)
            else :
                lab3 = Label(tk, text= saisi + " a gagné")
                lab3.pack(padx=5,pady=5)
            buttonRetour=Button(tk,text = "OK", command=tk.destroy)
            buttonRetour.pack(padx=5,pady=5)
            return
        if joueur2 == 5 :
            print('j2win')
            tk=Tk()
            tk.title("VAINQUEUR")
            tk.geometry('450x100')
            if saisi2 == "" :
                lab4 = Label(tk, text= "Le JOUEUR 2 a gagné")
                lab4.pack(padx=5,pady=5)
            else :
                lab4 = Label(tk, text= saisi2+ " a gagné")
                lab4.pack(padx=5,pady=5)
            buttonRetour=Button(tk,text = "OK", command=tk.destroy)
            buttonRetour.pack(padx=5,pady=5)
            return
        
        if perdu == False :
            canvas.after(20,deplacer) # Appel après 20 millisecondes
        else :
            # Les coordonnées de départ de la balle et sa vitesse
            x0, y0 = 405,270
            # La balle à déplacer
            canvas.coords(balle,x0,y0,x0+20,y0+20)
            time.sleep(0.1)
            deplacer()

        
        return



    #Une fonction pour le deplacement vers le haut de la raquette 1:
    def haut1(event):
        global deuy0
        if deuy0 >= 40 :
            deuy0=deuy0-40
        else :
            deuy0 = -30
        canvas.coords(raquette,20,deuy0,35,deuy0+100)
        
    #Une fonction pour le deplacement vers le bas de la raquette 1 :
    def bas1(event):
        global deuy0
        if deuy0 <= 400 :
            deuy0 = deuy0+40
        else :
            deuy0 = 470
        canvas.coords(raquette,20,deuy0,35,deuy0+100)

    #Une fonction pour le deplacement vers le haut de la raquette 2 :    
    def haut2(event):
        global troiy0
        if troiy0 >= 40 :
            troiy0=troiy0-40
        else :
            troiy0 = -30
        canvas.coords(raquette2,775,troiy0,790,troiy0+100)
        

    #Une fonction pour >le deplacement vers le bas de la raquette 2 :
    def bas2(event):
        global troiy0
        if troiy0 <= 400 :
             troiy0=troiy0+40
        else :
            troiy0 = 470
        canvas.coords(raquette2,775,troiy0,790,troiy0+100)









    
    root = tk.Toplevel()
    root.geometry('810x570')

    canvas = Canvas(root, width=810, height=540, bg='#5F9EA0') 
    imgjeu = PhotoImage(file = r"Fond pong gif.gif")
    canvas.create_image(0, 0, anchor=NW, image = imgjeu)
    canvas.place(x=0, y=0)

    root.title("Jeu De Pong")

    #On Créer la balle à déplacer
    balle = canvas.create_oval(x0,y0,x0+10,y0+10,width=1,fill="white")
    #On créer la raquette
    raquette = canvas.create_rectangle(20,deuy0,35,deuy0+100,fill='grey')
    #On créer la raquette deux
    raquette2 = canvas.create_rectangle(775,troiy0,790,troiy0+100,fill='#AF5573')


    #On associe les fleches du clavier aux fonctions haut1 et bas1 pour le joueur 1:
    canvas.bind_all('<z>', haut1)
    canvas.bind_all('<s>', bas1)
    #On associe les fleches du clavier aux fonctions haut2 et bas2 pour le joueur 2:
    canvas.bind_all('<Up>', haut2)
    canvas.bind_all('<Down>', bas2)

    #boutton quitter
    buttonQuitter=Button(root,text='Quitter',command=root.destroy)
    buttonQuitter.place(x = 460, y = 542.5 )

    #Boutton rejouer
    buttonRejouer=Button(root,text='Rejouer',command=rejouer)
    buttonRejouer.place(x = 380, y = 542.5 )

    #score des joueurs
    lab1=Label(root, text = "JOUEUR 1 : 0") # Initialisé à vide
    lab1.place(x = 50, y = 545)

    lab2=Label(root, text =  "JOUEUR 2 : 0") # Initialisé à vide
    lab2.place(x = 700, y = 545)

    button_commencer=Button(root,text = "Commencer",command=commencer)
    button_commencer.place(x = 300, y = 542.5 )



    root.mainloop()






def devinombre():
    global nbe, ten, tent, n, lvl, cmax


    def code() :
        global tent, n, lvl, cmax

        print(n)
        
        s2()
        
        if s == n :
            lab2.configure(text="Bien joué")
            lvl = lvl + 1
            tent = tent - 1
            lab3.configure(text=ten+str(tent))
            if lvl == 5 :
                messagebox.showinfo("Devi-Nombre", "BRAVO TU AS GAGNÉ")
            return
            
        elif s < n  :
            lab2.configure(text="Plus grand")
            tent = tent - 1

        elif s > n :
            lab2.configure(text="Plus petit")
            tent = tent - 1
            
        if tent <= 0 :
            lab2.configure(text="Tu as perdu")
            lab3.configure(text="Le nombre était " + str(n))
            return
        lab3.configure(text=ten+str(tent))

        
        




    def recommencer():
        global tent, n, lvl, cmax
        lvl = 1
        tent = 10
        cmax = 10
        n = randint(0, cmax)
        lab1.configure(text="Essaye de deviner un nombre 0 et "+str(cmax)+" :")
        lab2.configure(text="")
        lab3.configure(text=ten+str(tent))
        lab5.configure(text="Niveau "+str(lvl))   

    def nextlvl():
        global lvl, cmax, tent, n
        if lvl == 1 :
            cmax = 10
            n = randint(0, cmax)
            tent = 10
            lab1.configure(text="Essaye de deviner un nombre 0 et "+str(cmax)+" :")
            lab2.configure(text="")
            lab3.configure(text=ten+str(tent))
            lab5.configure(text="Niveau "+str(lvl))
        if lvl == 2 :
            cmax = 100
            n = randint(0, cmax)
            tent = 10
            lab1.configure(text="Essaye de deviner un nombre 0 et "+str(cmax)+" :")
            lab2.configure(text="")
            lab3.configure(text=ten+str(tent))
            lab5.configure(text="Niveau "+str(lvl))
        if lvl == 3 :
            cmax = 1000
            n = randint(0, cmax)
            tent = 10
            lab1.configure(text="Essaye de deviner un nombre 0 et "+str(cmax)+" :")
            lab2.configure(text="")
            lab3.configure(text=ten+str(tent))
            lab5.configure(text="Niveau "+str(lvl))
        if lvl == 4 :
            cmax = 10000
            n = randint(0, cmax)
            tent = 10
            lab1.configure(text="Essaye de deviner un nombre 0 et "+str(cmax)+" :")
            lab2.configure(text="")
            lab3.configure(text=ten+str(tent))
            lab5.configure(text="Niveau "+str(lvl))
            



    rootd = tk.Toplevel()
    rootd.title('Devinombre')
    rootd.geometry('450x120')

    lab1=Label(rootd,text="Essaye de deviner un nombre 0 et "+str(cmax)+" :")
    lab1.grid(row=0,column=0)

    lab2 = Label(rootd,text=" ")
    lab2.grid(row=1,column=0)

    lab3=Label(rootd,text=ten+str(tent))
    lab3.grid(row=2,column=0)

    lab4=Label(rootd,text=" ")
    lab4.grid(row=3,column=0)

    lab5=Label(rootd,text="Niveau "+str(lvl))
    lab5.grid(row=1,column=1)


    e1=Entry(rootd)
    e1.grid(row=0,column=1)


    b1=Button(rootd,text='OK',command=code)
    b1.grid(row=0,column=2)

    b2=Button(rootd,text="Quitter", command=rootd.destroy)
    b2.grid(row= 4,column=0)

    b3=Button(rootd,text="Recommencer", command=recommencer)
    b3.grid(row= 4,column=1)

    b4=Button(rootd,text="Niveau suivant", command=nextlvl)
    b4.grid(row= 4,column=2)
    


    def s2():
        global s
        s = int(e1.get())



    rootd.mainloop






def morpion():
    global clic, decompte, vert
    root = Tk()
    root.title('Morpion')

    # Pour ne plus pouvoir appuyer sur les boutons après la fin d'une partie
    def desactive():
        b1.configure(state = DISABLED)
        b2.configure(state = DISABLED)
        b3.configure(state = DISABLED)

        b4.configure(state = DISABLED)
        b5.configure(state = DISABLED)
        b6.configure(state = DISABLED)

        b7.configure(state = DISABLED)
        b8.configure(state = DISABLED)
        b9.configure(state = DISABLED)



    #fonction pour voir si quelqu'un a gagné
    def win():
        global gagnant, decompte
        gagnant = False
        
        #Pour les croix :
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" :
            gagnant = True
            b1.configure(bg = "red")
            b2.configure(bg = "red")
            b3.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" :
            gagnant = True
            b4.configure(bg = "red")
            b5.configure(bg = "red")
            b6.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b7.configure(bg = "red")
            b8.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" :
            gagnant = True
            b1.configure(bg = "red")
            b4.configure(bg = "red")
            b7.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" :
            gagnant = True
            b2.configure(bg = "red")
            b5.configure(bg = "red")
            b8.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b3.configure(bg = "red")
            b6.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")

            desactive()
            
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b1.configure(bg = "red")
            b5.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" :
            gagnant = True
            b3.configure(bg = "red")
            b5.configure(bg = "red")
            b7.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()


        #Pour les ronds :
        if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" :
            gagnant = True
            b1.configure(bg = "red")
            b2.configure(bg = "red")
            b3.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" :
            gagnant = True
            b4.configure(bg = "red")
            b5.configure(bg = "red")
            b6.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b7.configure(bg = "red")
            b8.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" :
            gagnant = True
            b1.configure(bg = "red")
            b4.configure(bg = "red")
            b7.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" :
            gagnant = True
            b2.configure(bg = "red")
            b5.configure(bg = "red")
            b8.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b3.configure(bg = "red")
            b6.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")

            desactive()
            
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b1.configure(bg = "red")
            b5.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" :
            gagnant = True
            b3.configure(bg = "red")
            b5.configure(bg = "red")
            b7.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()



        if decompte == 9 and gagnant == False :
            messagebox.showinfo("Morpion", "Match nul")
            desactive()
        


    def win_vert():
        global gagnant, decompte
        gagnant = False
        
        #Pour les croix :
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" :
            gagnant = True
            b1.configure(bg = "green")
            b2.configure(bg = "green")
            b3.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" :
            gagnant = True
            b4.configure(bg = "green")
            b5.configure(bg = "green")
            b6.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b7.configure(bg = "green")
            b8.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" :
            gagnant = True
            b1.configure(bg = "green")
            b4.configure(bg = "green")
            b7.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" :
            gagnant = True
            b2.configure(bg = "green")
            b5.configure(bg = "green")
            b8.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b3.configure(bg = "green")
            b6.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")

            desactive()
            
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b1.configure(bg = "green")
            b5.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" :
            gagnant = True
            b3.configure(bg = "green")
            b5.configure(bg = "green")
            b7.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()


        #Pour les ronds :
        if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" :
            gagnant = True
            b1.configure(bg = "green")
            b2.configure(bg = "green")
            b3.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" :
            gagnant = True
            b4.configure(bg = "green")
            b5.configure(bg = "green")
            b6.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b7.configure(bg = "green")
            b8.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" :
            gagnant = True
            b1.configure(bg = "green")
            b4.configure(bg = "green")
            b7.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" :
            gagnant = True
            b2.configure(bg = "green")
            b5.configure(bg = "green")
            b8.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b3.configure(bg = "green")
            b6.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")

            desactive()
            
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b1.configure(bg = "green")
            b5.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" :
            gagnant = True
            b3.configure(bg = "green")
            b5.configure(bg = "green")
            b7.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()



        if decompte == 9 and gagnant == False :
            messagebox.showinfo("Morpion", "Match nul")
            desactive()


    def win2():
        global gagnant, decompte
        gagnant = False
        
        #Pour les croix :
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" :
            gagnant = True
            b1.configure(bg = "red")
            b2.configure(bg = "red")
            b3.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" :
            gagnant = True
            b4.configure(bg = "red")
            b5.configure(bg = "red")
            b6.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b7.configure(bg = "red")
            b8.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" :
            gagnant = True
            b1.configure(bg = "red")
            b4.configure(bg = "red")
            b7.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" :
            gagnant = True
            b2.configure(bg = "red")
            b5.configure(bg = "red")
            b8.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b3.configure(bg = "red")
            b6.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b1.configure(bg = "red")
            b5.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" :
            gagnant = True
            b3.configure(bg = "red")
            b5.configure(bg = "red")
            b7.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            

        #Pour les ronds :
        if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" :
            gagnant = True
            b1.configure(bg = "red")
            b2.configure(bg = "red")
            b3.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" :
            gagnant = True
            b4.configure(bg = "red")
            b5.configure(bg = "red")
            b6.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b7.configure(bg = "red")
            b8.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" :
            gagnant = True
            b1.configure(bg = "red")
            b4.configure(bg = "red")
            b7.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" :
            gagnant = True
            b2.configure(bg = "red")
            b5.configure(bg = "red")
            b8.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b3.configure(bg = "red")
            b6.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b1.configure(bg = "red")
            b5.configure(bg = "red")
            b9.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" :
            gagnant = True
            b3.configure(bg = "red")
            b5.configure(bg = "red")
            b7.configure(bg = "red")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        if decompte == 9 and gagnant == False :
            messagebox.showinfo("Morpion", "Match nul")
            recommencer2()
        









    def win2_vert():
        global gagnant, decompte
        # si il reste False c'est match nul
        gagnant = False
        
        #Pour les croix :
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" :
            gagnant = True
            #change la couleur quand quelqu'un gagne
            b1.configure(bg = "green")
            b2.configure(bg = "green")
            b3.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" :
            gagnant = True
            b4.configure(bg = "green")
            b5.configure(bg = "green")
            b6.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b7.configure(bg = "green")
            b8.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" :
            gagnant = True
            b1.configure(bg = "green")
            b4.configure(bg = "green")
            b7.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" :
            gagnant = True
            b2.configure(bg = "green")
            b5.configure(bg = "green")
            b8.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b3.configure(bg = "green")
            b6.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            desactive()
            
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" :
            gagnant = True
            b1.configure(bg = "green")
            b5.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" :
            gagnant = True
            b3.configure(bg = "green")
            b5.configure(bg = "green")
            b7.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'X' ont gagné")
            recommencer2()
            

        #Pour les ronds :
        if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" :
            gagnant = True
            b1.configure(bg = "green")
            b2.configure(bg = "green")
            b3.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" :
            gagnant = True
            b4.configure(bg = "green")
            b5.configure(bg = "green")
            b6.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b7.configure(bg = "green")
            b8.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" :
            gagnant = True
            b1.configure(bg = "green")
            b4.configure(bg = "green")
            b7.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            desactive()
            
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" :
            gagnant = True
            b2.configure(bg = "green")
            b5.configure(bg = "green")
            b8.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b3.configure(bg = "green")
            b6.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" :
            gagnant = True
            b1.configure(bg = "green")
            b5.configure(bg = "green")
            b9.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" :
            gagnant = True
            b3.configure(bg = "green")
            b5.configure(bg = "green")
            b7.configure(bg = "green")
            messagebox.showinfo("Morpion", "Bravo, les 'O' ont gagné")
            recommencer2()
            
        if decompte == 9 and gagnant == False :
            messagebox.showinfo("Morpion", "Match nul")
            recommencer2()


        
    #fonction boutton cliqué
    def b_clic(b):
        global clic, decompte, reset
        
        if reset == False :
            #si le bouton est activé vert devient False et utilise une autre fonction win quiu va mettre les cases en vert
            if vert == True :
                if b["text"] ==  "" and clic == True :
                    b["text"] = "X"
                    clic = False
                    decompte += 1
                    win()
                elif b["text"] ==  "" and clic == False :
                    b["text"] = "O"
                    clic = True
                    decompte += 1
                    win()
                else :
                    messagebox.showerror("Morpion", "Cette case à déjà été sélectionnée.\nChoisis en une autre.")
                    
            else : 
                if b["text"] ==  "" and clic == True :
                    b["text"] = "X"
                    clic = False
                    decompte += 1
                    win_vert()
                elif b["text"] ==  "" and clic == False :
                    b["text"] = "O"
                    clic = True
                    decompte += 1
                    win_vert()
                else :
                    messagebox.showerror("Morpion", "Cette case à déjà été sélectionnée.\nChoisis en une autre.")



        elif reset == True :
            #si le bouton est activé vert devient False et utilise une autre fonction win quiu va mettre les cases en vert
            if vert == True :
                if b["text"] ==  "" and clic == True :
                    b["text"] = "X"
                    clic = False
                    decompte += 1
                    win2()
                elif b["text"] ==  "" and clic == False :
                    b["text"] = "O"
                    clic = True
                    decompte += 1
                    win2()
                else :
                    messagebox.showerror("Morpion", "Cette case à déjà été sélectionnée.\nChoisis en une autre.")
            else :
                if b["text"] ==  "" and clic == True :
                    b["text"] = "X"
                    clic = False
                    decompte += 1
                    win2_vert()
                elif b["text"] ==  "" and clic == False :
                    b["text"] = "O"
                    clic = True
                    decompte += 1
                    win2_vert()
                else :
                    messagebox.showerror("Morpion", "Cette case à déjà été sélectionnée.\nChoisis en une autre.")


        
    def recommencer() :
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clic, decompte, gagnant, reset

        reset = False
        gagnant = False
        clic = True
        decompte = 0

        #creation des bouttons
        b1 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b1))
        b2 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b2))
        b3 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b3))

        b4 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b4))
        b5 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b5))
        b6 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b6))

        b7 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b7))
        b8 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b8))
        b9 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b9))

        #placement des bouttons
        b1.grid(row = 0 , column = 0)
        b2.grid(row = 0 , column = 1)
        b3.grid(row = 0 , column = 2)

        b4.grid(row = 1 , column = 0)
        b5.grid(row = 1 , column = 1)
        b6.grid(row = 1 , column = 2)

        b7.grid(row = 2 , column = 0)
        b8.grid(row = 2 , column = 1)
        b9.grid(row = 2 , column = 2)



    def recommencer2() :
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clic, decompte, gagnant, reset

        reset = True
        gagnant = False
        clic = True
        decompte = 0

        #creation des bouttons
        b1 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b1))
        b2 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b2))
        b3 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b3))

        b4 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b4))
        b5 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b5))
        b6 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b6))

        b7 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b7))
        b8 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b8))
        b9 = Button(root, text = "", height = 3, width = 6, bg = 'white' , command = lambda: b_clic(b9))

        #placement des bouttons
        b1.grid(row = 0 , column = 0)
        b2.grid(row = 0 , column = 1)
        b3.grid(row = 0 , column = 2)

        b4.grid(row = 1 , column = 0)
        b5.grid(row = 1 , column = 1)
        b6.grid(row = 1 , column = 2)

        b7.grid(row = 2 , column = 0)
        b8.grid(row = 2 , column = 1)
        b9.grid(row = 2 , column = 2)







    def c_vert():
        global vert
        vert = False

    def c_rouge():
        global vert
        vert = True




    #crétion d'un menu
    mon_menu = Menu(root)
    root.configure(menu = mon_menu)

    #option du menu
    menu_options = Menu(mon_menu, tearoff = False)
    mon_menu.add_cascade(label = "Options", menu = menu_options)
    menu_options.add_command(label = "Recommencer le jeu", command = recommencer)

    menu_options.add_command(label = "Recommencer le jeu automatiquement", command = recommencer2)
    menu_options.add_command(label = "Changer la couleur du gagnant en vert", command = c_vert)
    menu_options.add_command(label = "Changer la couleur du gagnant en rouge", command = c_rouge)



    menu_options.add_command(label = "Quitter", command = root.destroy)


    

    recommencer()
    root.mainloop()



boutonjouer = PhotoImage(file="Bouton JOUER.png")
boutonregles = PhotoImage(file="Bouton REGLES.png")
boutonquitter = PhotoImage(file="Bouton QUITTER.png")
bm1 = tk.Button(fenetre, text ="Jouer",command = fenchoix,image=boutonjouer, bg="#FFE1E9",  height = 50, width = 140, relief=FLAT)
bm2 = tk.Button(fenetre, text ="Regles de jeux", command = fenregles,image=boutonregles, bg="#FFE1E9", height = 50, width = 140, relief=FLAT)
bm3 = tk.Button(fenetre, text ="Quitter",command = fenetre.destroy,image=boutonquitter, bg="#FFE1E9", height = 50, width = 140, relief=FLAT)


bm1.place(x=320, y=130) 
bm2.place(x=320, y=200) 
bm3.place(x=320, y=270) 








fenetre.mainloop()






lab2.configure(text="")


