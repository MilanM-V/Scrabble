from tkinter import*
from random import randint
from os import chdir
from tkinter import messagebox
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import customtkinter
import time
import os
import sys
connexion = Tk()
#creation de la connexion principale tkinter
connexion.title("Se connecter au jeu du mot le plus long")
connexion.geometry("500x500+400+100")
connexion.configure(bg="#FFE4B5")
accueil = Toplevel(connexion) #création de la fenetre princiaple "accueil"
accueil.withdraw()
crea=Toplevel(connexion) # création de la fenetre "crea"
crea.withdraw()
select=Toplevel(connexion) #création de la fenetre " select
select.withdraw()
finale=Toplevel(connexion) #création de la fenetre "finale"
finale.withdraw()
regles = Toplevel(connexion) #création de la fenêtre des "regles"
regles.withdraw()
best=Toplevel(connexion) #création de la fenêtre des "regles"
best.withdraw()
best2=Toplevel(connexion) #création de la fenêtre des "best2"
best2.withdraw()
color=Toplevel(connexion) #création de la fenêtre des "color"
color.withdraw()
objectif=Toplevel(connexion) #création de la fenêtre des "objectif"
objectif.withdraw()
objectif2=Toplevel(connexion)
objectif2.withdraw()
Stat=Toplevel(connexion) #création de la fenêtre des "Stat"
Stat.withdraw()
mode=Toplevel(connexion) #création de la fenêtre des "mode"
mode.withdraw()
liste=[] #création de la liste "liste"
roster=[] #création de la liste "roster"
fonction=0 #création de la variable "fonction"
list_mot=[] #création de la liste "list_mot"
iterations=0 #création de la variable "iteration"
liste_label=[] #création de la liste "liste_label"
score=0 #création de la variable "score"
score_marathon=0 #création de la variable "score_marathon"
genre=[] #création de la liste "genre"
couleur="#FFE4B5" #création de la variable "couleur" et couleur du début
mode_jeu="" 
marathon_liste=[] #création de la liste "marathon_liste"
multiplicateur=0 #création de la variable "multiplicateur"
chemins = ["./donnees/compte.csv", "./compte.csv"] #differend chemin pour acceder à "compte.csv"
chemins1=["./images/book_3725.ico","./book_3725.ico"] #differend chemin pour acceder à "book_3725.ico"
list_valid=[] #création de la liste "list_valid"
btn_state = False
bandeau_deroulant_existe = False
#Chargement des images
nav_icon = PhotoImage(file="./images/navbar.png")
close_icon = PhotoImage(file="images/close.png")
dictionnaire="liste_finale.txt"

def quits(): #fonction pour quitter le jeu
    if 'temps_debut' in globals():
        temps_fin = time.time()
        for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="r", newline='') as fichier_csv:
                    lecteur_csv = csv.DictReader(fichier_csv)
                    donnees = list(lecteur_csv)
        try:
            for ligne in donnees:
                if ligne["Pseudo"]==username:
                    ligne["dernier_temps"] = int(temps_fin - temps_debut)
        except:
            sys.exit()
        for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="w", newline='') as fichier_csv:
                    noms_colonnes = ["Pseudo", "Mdp","total_sprint","total_marathon","ach1","ach2", "ach3","ach4","ach5","ach6","ach7","ach8","ach9","ach10","ach11","ach12","ach13","ach14","ach15","ach16","nb_partie_sprint","nb_partie_marathon","9","8","7","6","5","4","3","2","1","Score_sprint","Score_mara","nb_mot_marathon","dernier_temps"]               
                    ecrivain = csv.DictWriter(fichier_csv, fieldnames=noms_colonnes)
                    ecrivain.writeheader()
                    ecrivain.writerows(donnees)
    sys.exit()

def page_accueil(): #fonction  da la page d'accueil
    global bandeau_deroulant_existe,frame,zone_texte
    mettre_à_jour_donnees_vide() #appel de la fonction 
    connexion.withdraw()
    accueil.deiconify()
    #parametre de la page accueil
    accueil.title("Accueil")
    accueil.geometry("500x500+400+100")
    accueil.config(bg = couleur)
    #créaion de label
    zone_texte = Label (accueil,text = "Bienvenue sur la page d'accueil de \n \"Le mot le plus long\" ",font=('Aldus', 16,'bold'), bg=couleur)
    zone_texte.place(x=80, y=100)
    zone_texte.lower()
    #création des bouton "Mode de jeu", "quitter", "règle", "Classement", "fond", "achivement" et "compte"
    btn_mode = customtkinter.CTkButton(accueil,text="Cliquez sur le bouton\npour commencer",border_width=1,height=70, width=250,text_color='black',border_color='black',fg_color="#34C0E2",hover_color="#E8E8E8", command=mod)
    btn_mode.place(x=130, y=260)
    quitter = customtkinter.CTkButton(accueil,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=430, y=11)
    def optionmenu_callback(choice):
        global dictionnaire
        if choice =="Français":
            dictionnaire="liste_finale.txt"
        elif choice=="Anglais":
            dictionnaire="words_anglais.txt"
        elif choice=="Indonésien":
            dictionnaire="00-indonesian-wordlist.txt"
        elif choice=="Italien":
            dictionnaire="italian_words.txt"
    optionmenu_var = customtkinter.StringVar(value="Français")
    optionmenu = customtkinter.CTkOptionMenu(accueil, values=["Français", "Anglais","Indonésien","Italien"],
                                         command=optionmenu_callback,
                                         variable=optionmenu_var)
    optionmenu.place(x=190,y=40)
    explication=Label(accueil,text="Choisissez la langue du dictionnaire :",bg=couleur)
    explication.place(x=160,y=10)
    #Création du frame principal
    frame = Frame(accueil, bg=couleur,height=40,width=500)
    
    frame.pack(side="top", fill=X)
    frame.lower()
    #Fonction pour basculer l'affichage du menu
    def switch():
        global btn_state
        if btn_state is True:
            for x in range(251):
                NavBar.place(x=-x, y=0)
                frame.update()
            frame.config(bg=couleur)
            btn_state = False
        else:
            for x in range(-250, 0):
                NavBar.place(x=x, y=0)
                frame.update()
            frame.config(bg=couleur)
            btn_state = True
    
    #Bouton pour ouvrir le menue
    navbar_btn = Button(frame, image=nav_icon, bg='black', bd=0, command=switch)
    navbar_btn.grid(row=1, column=1)

    #Création du menu déroulant
    NavBar = Frame(accueil, bg='black', height=1000, width=250)
    NavBar.place(x=-250, y=0)
    NavBar.lift()

    #Bouton du menue deroulant appelant des fonctions
    règle = Button(NavBar,text="règle",font='artel 18 bold', bg='black', fg="white", activebackground='gray', activeforeground='white', bd=0, command=lambda: [regle(), switch()])
    règle.place(x=25, y=60)
    classement= Button(NavBar,text="Classement",font='artel 18 bold', bg='black', fg="white", activebackground='gray', activeforeground='white', bd=0, command=lambda: [rank(), switch()])
    classement.place(x=25,y=110)
    bg= Button(NavBar,text="Fond",font='artel 18 bold', bg='black', fg="white", activebackground='gray', activeforeground='white', bd=0, command=lambda: [fond(), switch()])
    bg.place(x=25,y=160)
    btn_achivement= Button(NavBar,text="Achivement",font='artel 18 bold', bg='black', fg="white", activebackground='gray', activeforeground='white', bd=0, command=lambda: [pg_achivement(), switch()])
    btn_achivement.place(x=25,y=210)
    btn_compte=Button(NavBar,text="Compte",font='artel 18 bold', bg='black', fg="white", activebackground='gray', activeforeground='white', bd=0, command=lambda: [compte(), switch()])
    btn_compte.place(x=25,y=260)

    #Bouton pour fermer le menu
    close_btn = Button(NavBar, image=close_icon, bg='black', bd=0, command=switch)
    close_btn.place(x=200, y=5)
    quitter.lift()

def regle(): #fonction de l'affichage de la fenetre regle
    accueil.withdraw()
    regles.deiconify()
    #parametre de la fenetre "regles"
    regles.title("Les règles du jeu") 
    for chemin in chemins1:
        if os.path.exists(chemin):
            regles.iconbitmap(chemin)
    regles.config(bg = couleur)
    regles.geometry("510x510+400+100")
    #création des boutons quitter et retour
    quitter = customtkinter.CTkButton(regles,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=442, y=11)
    retour = customtkinter.CTkButton(regles, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)#creation du bouton de retour à l'accueil
    retour.place(x= 30, y=11)
    #création de label pour afficher les règles
    texte1 = Label(regles, text = "Voici les règles du jeu du mot le plus long :", font=('Helvetica 15 underline', 17),bg=couleur)
    texte1.pack()
    texte1.place(x=48, y=100)
    texte2 = Label(regles, text= "-Le but du jeu 'Le mot le plus long' est de, à partir de 9 lettres tirées au hasard, construire le", justify="center",bg=couleur)
    texte2.place(x=0, y=180)
    texte2bis = Label(regles, text= "mot le plus long que l'on puisse imaginer. Si on ne peut pas trouver un mot en 9, on cherche en", justify="center",bg=couleur)
    texte2bis.place(x=0, y=200)
    texte2tris = Label(regles, text="8 lettres et ainsi de suite, jusqu'à ce que l'on trouve.", justify="center",bg=couleur)
    texte2tris.place(x=0, y=220)
    texte3 = Label(regles, text="-Le tirage de lettres se fait au hasard, on demande au joueur quel type de lettre il désire (voyelle", justify="center",bg=couleur)
    texte3.place(x=0, y=240)
    texte3bis = Label(regles, text=" ou consonne) ainsi de suite jusqu'à ce qu'il en ait 9. Il lui faut minimum 3 voyelles", justify="center",bg=couleur)
    texte3bis.place(x=0, y=260)
    text4=Label(regles,text="Explication des modes de jeu :\n\nMarathon : Le mode marathon consiste à trouver le maximum de mot en 300 secondes.\n\nSprint : Le mode sprint consiste à trouver un mot le plus rapidement possible en 50 secondes.", justify="left",bg=couleur)
    text4.place(x=10,y=290)

def creation_mot(): #fonction de la fenetre pour creer les mots
    global duree,marathon_liste,list_valid
    select.withdraw()
    crea.deiconify()
    #parametre de la page crea
    crea.title("Jeu")
    crea.geometry("500x500+400+100")
    crea.config(bg = couleur)
    #fonction du timer
    def chrono():
        text_timer=Label(crea,text=str(duree)+"s",bg=couleur,font=(12))
        text_timer.place(x=230,y=400)
        crea.after(1000,chrono)
    chrono()
    def extraire(): #fonction pour extraire les informations du document
        global donnees,iterations
        chdir("./donnees/")
        fichier = open(dictionnaire)
        donnees =fichier.readlines()
        fichier.close()
        iterations+=1
    if iterations<=0:#appel de la fonction extraire
        extraire()
    #création du label 
    zone_texte_3 = Label(crea, text="Cliquer-glisser les lettres dans le bon ordre\n de gauche à droite",font=('arial',14,'bold'), bg=couleur)
    zone_texte_3.place(x=40, y=180)
    def valid(): #fonction pour verifier l'existence du mot dans le dictionnaire
        global  list_valid,marathon_liste,genre
        for element in donnees:
            element=element.rstrip("\n")
            ligne=element.split(";")
            list_mot.append(ligne)
        list_valid = ["".join(roster)]
        mot_valid=""
        for mots in list_mot:
            if list_valid == mots: #vérification de l'existance du mot dans le dictionnaire
                mot_valid="Oui"
                list_valid="".join(list_valid)
                if mode_jeu=="marathon": #si le mode de jeu marathon
                    if duree <= 0:    #quand le timer est à 0
                        select.withdraw()
                        crea.withdraw()
                        genre=marathon_liste
                        final()
                    else: 
                        marathon_liste.append(list_valid)
                        marathon_recommencer()
                        genre=marathon_liste
                elif mode_jeu=="sprint":
                    genre=list_valid
                    final()           
        if mot_valid!="Oui":
            zone_texte_8 = Label(crea, text="Le mot n'existe pas", bg="red")
            zone_texte_8.place(x=200, y=340)
    #création des buttons
    valider=Button(crea, text="Valider",heigh=5,width=20, bg="#2AFF00", command=valid)
    valider.place(x=275,y=370)
    reinitialiser=Button(crea, text="Reinitialiser",heigh=5,width=20, bg="#FF5500", command=reinitialiser_page)
    reinitialiser.place(x=75,y=370)
    retour = customtkinter.CTkButton(crea, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)
    retour.place(x= 10, y=5)
    quitter = customtkinter.CTkButton(crea,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=440,y=5)
    btn_recommencer = Button(crea, bg="#D5C935", text="Recommencer", command=recommencer)
    btn_recommencer.place(x=220, y =470)
    arreter=Button(crea,text="Arreter",bg="#D5C935",command=stop)
    if mode_jeu=="marathon":
        btn_recommencer.place(x=260,y=470)
        arreter.place(x=200,y=470)

def final():
    global score,duree,genre,score_marathon
    crea.withdraw()
    select.withdraw()
    finale.deiconify()
    finale.title("Jeu")
    finale.geometry("500x500+400+100")
    finale.config(bg = couleur)
    bj=duree
    #modification du multipicateur en fonction du temps restant
    if duree==50 or duree>=40:
        multiplicateur=1.5
    elif duree==39 or duree>=30:
        multiplicateur=1.3
    elif duree==29 or duree >=20:
        multiplicateur=1
    elif duree==19 or duree>=10:
        multiplicateur=0.85
    elif duree==9 or duree>=0:
        multiplicateur=0.75
    duree=-35
    def mot_long():
        global longeur_liste,keep,lettres,mot,liste
        liste_save=liste[:]
        keep=[]
        mot=[]
        for mot in list_mot:
            for lettres in mot:
                lettres=list(lettres)
                longeur_liste=0
                liste=liste_save[:]
                mot=[]
                mot_le_plus_long()
    #cherche le mot le plus long du dictionnaire avec les lettre à dispositioj
    def mot_le_plus_long():
        global longeur_liste, mot, keep
        for lettre in liste:
            if not longeur_liste==len(lettres):
                if lettre in lettres[longeur_liste]:
                    longeur_liste+=1
                    mot.append(lettre)
                    liste.remove(lettre)
                    mot_le_plus_long()
            else:
                if len(keep)<len(mot):
                    keep=[]
                    keep="".join(mot)
    mot_long()
    #ouverture du csv en mode lecture
    for chemin in chemins:
        if os.path.exists(chemin):
            with open(chemin, mode="r", newline='') as fichier_csv:
                lecteur_csv = csv.DictReader(fichier_csv)
                donnees = list(lecteur_csv)
            break
    for ligne in donnees:
            #augmente de 1 le nb de partie jouer du mode sprint dans le csv
            if mode_jeu=="sprint":
                if ligne["Pseudo"]==username:
                    if ligne["nb_partie_sprint"] is not None and ligne["nb_partie_sprint"] != '':
                        ligne["nb_partie_sprint"]=int(ligne["nb_partie_sprint"])+1
                    else:
                        ligne["nb_partie_sprint"]=1
            #augmente de 1 le nb de partie jouer du mode marathon dans le csv
            elif mode_jeu=="marathon":
                if ligne["Pseudo"]==username:
                    if ligne["nb_partie_marathon"] is not None and ligne["nb_partie_marathon"] != '':
                        ligne["nb_partie_marathon"]=int(ligne["nb_partie_marathon"])+1
                    else:
                        ligne["nb_partie_marathon"]=1
            #calcule des point et modif du csv en fonction du nombre de lettres du mots trouver en sprint
            if mode_jeu == 'sprint':
                if len(genre)==9:
                    score=100*multiplicateur
                    if ligne["Pseudo"]==username:
                        if ligne["9"] is not None and ligne["9"] != '':
                            ligne["9"] = int(ligne["9"]) + 1 #Modifie la valeur dans la colonne spécifiée
                        else:
                            ligne["9"]=1
                elif len(genre)==8:
                    score=80*multiplicateur
                    if ligne["Pseudo"]==username:
                        if ligne["8"] is not None and ligne["8"] != '':
                            ligne["8"] = int(ligne["8"]) + 1 #Modifie la valeur dans la colonne spécifiée
                        else:
                            ligne["8"]=1
                elif len(genre)==7:
                    score=70*multiplicateur
                    if ligne["Pseudo"]==username:
                        if ligne["7"] is not None and ligne["7"] != '':
                            ligne["7"] = int(ligne["7"]) + 1 #Modifie la valeur dans la colonne spécifiée
                        else:
                            ligne["7"]=1
                elif len(genre)==6:
                    score=60*multiplicateur
                    if ligne["Pseudo"]==username:
                        if ligne["6"] is not None and ligne["6"] != '':
                            ligne["6"] = int(ligne["6"]) + 1 #Modifie la valeur dans la colonne spécifiée
                        else:
                            ligne["6"]=1
                elif len(genre)==5:
                    score=50*multiplicateur
                    if ligne["Pseudo"]==username:
                        if ligne["5"] is not None and ligne["5"] != '':
                            ligne["5"] = int(ligne["5"]) + 1 #Modifie la valeur dans la colonne spécifiée
                        else:
                            ligne["5"]=1
                elif len(genre)==4:
                    score=40*multiplicateur
                    if ligne["Pseudo"]==username:
                        if ligne["4"] is not None and ligne["4"] != '':
                            ligne["4"] = int(ligne["4"]) + 1 #Modifie la valeur dans la colonne spécifiée
                        else:
                            ligne["4"]=1
                elif len(genre)==3:
                    score=30*multiplicateur
                    if ligne["Pseudo"]==username:
                        if ligne["3"] is not None and ligne["3"] != '':
                            ligne["3"] = int(ligne["3"]) + 1 #Modifie la valeur dans la colonne spécifiée
                        else:
                            ligne["3"]=1
                elif len(genre)==2:
                    score=20*multiplicateur
                    if ligne["Pseudo"]==username:
                        if ligne["2"] is not None and ligne["2"] != '':
                            ligne["2"] = int(ligne["2"]) + 1 #Modifie la valeur dans la colonne spécifiée
                        else:
                            ligne["2"]=1
                elif len(genre)==1:
                    score=10*multiplicateur
                    if ligne["Pseudo"]==username:
                        if ligne["1"] is not None and ligne["1"] != '':
                            ligne["1"] = int(ligne["1"]) + 1 #Modifie la valeur dans la colonne spécifiée
                        else:
                            ligne["1"]=1
            #calcule des point et modif du csv en fonction du nombre de lettres des mots trouver en marathon
            if mode_jeu=="marathon":
                score_marathon=0
                for mot in genre:
                    if len(mot)==9:
                        score_marathon+=100
                        if ligne["Pseudo"]==username:
                            if ligne["9"] is not None and ligne["9"] != '':
                                ligne["9"] = int(ligne["9"]) + 1 #Modifie la valeur dans la colonne spécifiée
                            else:
                                ligne["9"]=1
                    if len(mot)==8:
                        score_marathon+=80
                        if ligne["Pseudo"]==username:
                            if ligne["8"] is not None and ligne["8"] != '':
                                ligne["8"] = int(ligne["8"]) + 1 #Modifie la valeur dans la colonne spécifiée
                            else:
                                ligne["8"]=1
                    if len(mot)==7:
                        score_marathon+=70
                        if ligne["Pseudo"]==username:
                            if ligne["7"] is not None and ligne["7"] != '':
                                ligne["7"] = int(ligne["7"]) + 1 #Modifie la valeur dans la colonne spécifiée
                            else:
                                ligne["7"]=1
                    if len(mot)==6:
                        score_marathon+=60
                        if ligne["Pseudo"]==username:
                            if ligne["6"] is not None and ligne["6"] != '':
                                ligne["6"] = int(ligne["6"]) + 1 #Modifie la valeur dans la colonne spécifiée
                            else:
                                ligne["6"]=1
                    if len(mot)==5:
                        score_marathon+=50
                        if ligne["Pseudo"]==username:
                            if ligne["5"] is not None and ligne["5"] != '':
                                ligne["5"] = int(ligne["5"]) + 1 #Modifie la valeur dans la colonne spécifiée
                            else:
                                ligne["5"]=1
                    if len(mot)==4:
                        score_marathon+=40
                        if ligne["Pseudo"]==username:
                            if ligne["4"] is not None and ligne["4"] != '':
                                ligne["4"] = int(ligne["4"]) + 1 #Modifie la valeur dans la colonne spécifiée
                            else:
                                ligne["4"]=1
                    if len(mot)==3:
                        score_marathon+=30
                        if ligne["Pseudo"]==username:
                            if ligne["3"] is not None and ligne["3"] != '':
                                ligne["3"] = int(ligne["3"]) + 1 #Modifie la valeur dans la colonne spécifiée
                            else:
                                ligne["3"]=1
                    if len(mot)==2:
                        score_marathon+=20
                        if ligne["Pseudo"]==username:
                            if ligne["2"] is not None and ligne["2"] != '':
                                ligne["2"] = int(ligne["2"]) + 1 #Modifie la valeur dans la colonne spécifiée
                            else:
                                ligne["2"]=1
                    if len(mot)==1:
                        score_marathon+=10
                        if ligne["Pseudo"]==username:
                            if ligne["1"] is not None and ligne["1"] != '':
                                ligne["1"] = int(ligne["1"]) + 1 #Modifie la valeur dans la colonne spécifiée
                            else:
                                ligne["1"]=1

    for ligne in donnees:
        if ligne["Pseudo"]==username:
            if mode_jeu=="sprint":
                #mets à jour le meilleur score en mode sprint
                if ligne["Score_sprint"] is not None and ligne["Score_sprint"] != '':
                    if score>float(ligne["Score_sprint"]):
                        ligne["Score_sprint"]=score
                else:
                    ligne["Score_sprint"]=score
            if mode_jeu=="marathon":
                #mets à jour le meilleur score en mode marathon
                if ligne["Score_mara"] is not None and ligne["Score_mara"] != '':
                    if score_marathon>int(ligne["Score_mara"]):
                        ligne["Score_mara"]=score_marathon
                else:
                    ligne["Score_mara"]=score_marathon
                #mets à jour le nombre de mots max trouver en mode marathon
                if ligne["nb_mot_marathon"] is not None and ligne["nb_mot_marathon"] != '':
                    if len(genre)>int(ligne['nb_mot_marathon']):
                        ligne['nb_mot_marathon']=len(genre)
                else:
                    ligne['nb_mot_marathon']=len(genre)
    #ouvre le csv en mode écriture
    with open("./compte.csv", mode="w", newline='') as fichier_csv:
            noms_colonnes = ["Pseudo", "Mdp","total_sprint","total_marathon","ach1","ach2", "ach3","ach4","ach5","ach6","ach7","ach8","ach9","ach10","ach11","ach12","ach13","ach14","ach15","ach16","nb_partie_sprint","nb_partie_marathon","9","8","7","6","5","4","3","2","1","Score_sprint","Score_mara","nb_mot_marathon","dernier_temps"]               
            ecrivain = csv.DictWriter(fichier_csv, fieldnames=noms_colonnes)
            ecrivain.writeheader()
            ecrivain.writerows(donnees)
    fichier_csv.close()
    if liste!=[]:
        contenu_etiquette = ",".join(liste) #separe la liste par des virgules
    else:
        contenu_etiquette=""
    if mode_jeu=="marathon":
        #création des label si aucun mots trouver en mode marathon
        if marathon_liste==[] or list_valid==None:
            zone_texte_7=Label(finale,text="C'est dommage\nvous n'avez rien trouvé",bg=couleur, font=('Font Families', 20))
            zone_texte_7.place(x=120,y=150)
        #création des label si mot trouver en mode marathon
        else:
            zone_texte_1 = Label(finale, text="Bravo\nVous avez trouvé les mots : \n" + ", ".join(marathon_liste), font=('Aldus', 20), bg=couleur)
            zone_texte_1.place(x=100, y=100)
            zone_texte_5 = Label(finale, text="Vous avez obtenu le score de " + str(score_marathon), font=('Font Families', 20), bg=couleur,justify="center")
            zone_texte_5.place(x=40, y=40)
            point(username, score_marathon)
    if mode_jeu=="sprint":
        #création des label si aucun mot trouver en mode sprint
        if list_valid==[] or list_valid==None or genre==[]:
            zone_texte_6=Label(finale,text="C'est dommage\nvous n'avez rien trouvé",bg=couleur, font=('Font Families', 20))
            zone_texte_6.place(x=100,y=150)
        #création des label si le mot trouver est le plus long en mode sprint
        elif len(list_valid)>=len(keep):
            zone_texte_1 = Label(finale, text="Bravo\nVous avez trouver le mot \""+ list_valid+"\" en "+str(bj)+"s", font=('Aldus', 20), bg=couleur)
            zone_texte_1.place(x=60, y=100)
            zone_texte_5 = Label(finale, text="Vous avez obtenu le score de " + str(score), font=('Font Families', 20), bg=couleur,justify="center")
            zone_texte_5.place(x=40, y=40)
            point(username, score)
        #création des labels si le mots trouver n'est pas le plus long en mode sprint
        elif len(list_valid)<len(keep):
            zone_texte_2 = Label(finale, text="Bravo\nVous avez trouveé \""+ list_valid+"\" en "+str(bj)+"s", font=('Aldus', 20), bg=couleur, justify="center")
            zone_texte_2.place(x=80, y=80)
            zone_texte_3 = Label(finale, text="Avec ces lettres : " +contenu_etiquette +"\nVous auriez pu trouver \""+ keep+"\"\n avec "+str(len(keep)) + " lettres", font=('Font Families', 20), bg=couleur,justify="center")
            zone_texte_3.place(x=60, y=150)
            zone_texte_4 = Label(finale, text="Vous avez obtenu le score de " + str(score), font=('Font Families', 20), bg=couleur,justify="center")
            zone_texte_4.place(x=40, y=40)
            point(username, score)
    #création des bouton
    btn_recommencer = Button(finale, bg="#D5C935", text="Recommencer",height=10, width=20, command=recommencer)
    btn_recommencer.place(x=60, y =280)
    quitter = Button(finale, text="Quitter", bg="red",height=10, width=20, command=quits)
    quitter.place(x=300, y=280)
    retour = customtkinter.CTkButton(finale, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)
    retour.place(x= 10, y=5)

#fonction pour recommencer qui réinitialise tout à 0
def recommencer():
    global fonction, liste, liste_label, roster, list_mot,select,crea,finale,score,duree,marathon_liste,multiplicateur,list_valid,keep
    crea.destroy()
    select.destroy()
    finale.destroy()
    crea=Toplevel(accueil)
    crea.withdraw()
    select=Toplevel(accueil)
    select.withdraw()
    finale=Toplevel(accueil)
    finale.withdraw()
    liste=[]
    roster=[]
    liste_label=[]
    fonction=0
    if mode_jeu=="sprint":
        duree=50
    if mode_jeu=="marathon":
        duree=300
    list_mot=[]
    DragManager.listeDrop=[]
    score=0
    marathon_liste=[]
    multiplicateur=0
    list_valid=None
    keep=[]
    selection()

#fonction pour retourner à l'accueil qui réinitiale tout à 0
def retour_accueil():
    global fonction, liste, liste_label,marathon_liste, roster, list_mot,select,crea,finale,score,duree,marathon_liste,mode_jeu,list_valid,multiplicateur,btn_recommencer,arreter,genre,keep
    crea.destroy()
    select.destroy()
    finale.destroy()
    crea=Toplevel(accueil)
    crea.withdraw()
    select=Toplevel(accueil)
    select.withdraw()
    finale=Toplevel(accueil)
    finale.withdraw()
    mode.withdraw()
     #fermeture des fenetre
    finale.withdraw()
    regles.withdraw()
    color.withdraw()
    best.withdraw()
    best2.withdraw()
    objectif.withdraw()
    objectif2.withdraw()
    Stat.withdraw()
    liste=[]
    roster=[]
    liste_label=[]
    fonction=0
    if mode_jeu=="sprint":
        duree=50
    if mode_jeu=="marathon":
        duree=300
    list_mot=[]
    DragManager.listeDrop=[]
    score=0
    marathon_liste=[]
    mode_jeu=""
    list_valid=[]
    multiplicateur=0
    frame.destroy()
    zone_texte.destroy()
    genre=[]
    keep=[]
    marathon_liste=[]
    page_accueil()

#fonction pour que recommencer en mode marathon tant que la duree est au dessus de 0
def marathon_recommencer():
    global fonction, liste, liste_label, roster, list_mot,select,crea,finale,score
    crea.destroy()
    select.destroy()
    finale.destroy()
    crea=Toplevel(accueil)
    crea.withdraw()
    select=Toplevel(accueil)
    select.withdraw()
    finale=Toplevel(accueil)
    finale.withdraw()
    liste=[]
    roster=[]
    liste_label=[]
    fonction=0
    list_mot=[]
    DragManager.listeDrop=[]
    selection()
#fonction pour arreter le mode marathon
def stop():
    global duree
    duree=0

#création de la class dragManager pour pouvoir creer les mots
class DragManager():
        global reinitialiser_page,roster,liste_label
        listeDrop = []
        def __init__(self,widget,drag=True,drop=True):
            self.widget = widget
            self.drag = drag
            self.drop = drop
            if drag:
                self.add_dragable(self.widget)
            if drop:
                DragManager.listeDrop.append(self.widget)
        def add_dragable(self, widget):
            self.widget = widget
            self.widget.bind("<ButtonPress-1>", self.on_start)
            self.widget.bind("<B1-Motion>", self.on_drag)
            self.widget.bind("<ButtonRelease-1>", self.on_drop)
            self.widget["cursor"] = "hand1"
        def on_start(self, event):
            self.memoire = self.widget.cget("text")
        def on_drag(self, event):
            pass
        def on_drop(self, event):
            global roster,target
            x,y = event.widget.winfo_pointerxy()
            target = event.widget.winfo_containing(x,y)
            if target in DragManager.listeDrop:
                try:
                    target.configure(text=self.memoire)
                    self.widget.configure(text="")
                    roster.append(self.memoire)
                    liste_label.append(target)
                    DragManager.listeDrop.remove(self.widget)
                    
                except:
                    pass
            else:
                self.widget.configure(text=self.memoire)
        #fonction pour réinitialiser les widget
        def reinitialiser_page():
            global roster
            for widget in DragManager.listeDrop:
                widget.configure(text="")
            roster=[]
            DragManager.listeDrop=[]
            drag()
            if fonction==1:
                neuf()
            elif fonction==2:
                huit()
            elif fonction ==3:
                sept()
            elif fonction ==4:
                six()
            elif fonction ==5:
                cinq()
            elif fonction ==6:
                quatre()
            elif fonction ==7:
                trois()
            elif fonction ==8:
                deux()
            elif fonction ==9:
                un()
#fonction des label pour drop
def label_drop():
    global zoneDrop1,zoneDrop2,zoneDrop3,zoneDrop4,zoneDrop5,zoneDrop6,zoneDrop7,zoneDrop8,zoneDrop9,drop1,drop2,drop3,drop4,drop5,drop6,drop7,drop8,drop9
    # Création des 9 Labels dropables
    zoneDrop1 = Label(crea, text="", fg="white",relief="solid", highlightbackground=couleur, highlightthickness=2, bg="black", font=("Helvetica", 20), height=2, width=3)
    zoneDrop2 = Label(crea, text="",fg="white",relief="solid", highlightbackground=couleur, highlightthickness=2, bg="black",font=("Helvetica", 20),height = 2, width=3)
    zoneDrop3 = Label(crea, text="",fg="white",relief="solid", highlightbackground=couleur, highlightthickness=2, bg="black",font=("Helvetica", 20),height = 2, width=3)
    zoneDrop4 = Label(crea, text="",fg="white",relief="solid", highlightbackground=couleur, highlightthickness=2, bg="black",font=("Helvetica", 20),height = 2, width=3)
    zoneDrop5 = Label(crea, text="",fg="white",relief="solid", highlightbackground=couleur, highlightthickness=2, bg="black",font=("Helvetica", 20),height = 2, width=3)
    zoneDrop6 = Label(crea, text="",fg="white",relief="solid", highlightbackground=couleur, highlightthickness=2, bg="black",font=("Helvetica", 20),height = 2, width=3)
    zoneDrop7 = Label(crea, text="",fg="white",relief="solid", highlightbackground=couleur, highlightthickness=2, bg="black",font=("Helvetica", 20),height = 2, width=3)
    zoneDrop8 = Label(crea, text="",fg="white",relief="solid", highlightbackground=couleur, highlightthickness=2, bg="black",font=("Helvetica", 20),height = 2, width=3)
    zoneDrop9 = Label(crea, text="",fg="white",relief="solid", highlightbackground=couleur, highlightthickness=2, bg="black",font=("Helvetica", 20),height = 2, width=3)
    # Création des 9 objets autorisant le drag et aussi de ceux qui autorisent le drop
    drop1 = DragManager(zoneDrop1)
    drop2 = DragManager(zoneDrop2)
    drop3 = DragManager(zoneDrop3)
    drop4 = DragManager(zoneDrop4)
    drop5 = DragManager(zoneDrop5)
    drop6 = DragManager(zoneDrop6)
    drop7 = DragManager(zoneDrop7)
    drop8 = DragManager(zoneDrop8)
    drop9 = DragManager(zoneDrop9)

#placement des zones de drop et de choix en fonction du nombre choisi
def neuf():
    global fonction
    label_drop()
    choix1.place(x=30,y=50)
    choix2.place(x=80,y=50)
    choix3.place(x=130,y=50)
    choix4.place(x=180,y=50)
    choix5.place(x=230,y=50)
    choix6.place(x=280,y=50)
    choix7.place(x=330,y=50)
    choix8.place(x=380,y=50)
    choix9.place(x=430,y=50)
    zoneDrop1.place(x=30,y=250)
    zoneDrop2.place(x=80,y=250)
    zoneDrop3.place(x=130,y=250)
    zoneDrop4.place(x=180,y=250)
    zoneDrop5.place(x=230,y=250)
    zoneDrop6.place(x=280,y=250)
    zoneDrop7.place(x=330,y=250)
    zoneDrop8.place(x=380,y=250)
    zoneDrop9.place(x=430,y=250)
    fonction = 1
    creation_mot()

def huit():
    global fonction
    label_drop()
    choix1.place(x=30,y=50)
    choix2.place(x=80,y=50)
    choix3.place(x=130,y=50)
    choix4.place(x=180,y=50)
    choix5.place(x=230,y=50)
    choix6.place(x=280,y=50)
    choix7.place(x=330,y=50)
    choix8.place(x=380,y=50)
    choix9.place(x=430,y=50)
    zoneDrop1.place(x=45,y=250)
    zoneDrop2.place(x=95,y=250)
    zoneDrop3.place(x=145,y=250)
    zoneDrop4.place(x=195,y=250)
    zoneDrop5.place(x=245,y=250)
    zoneDrop6.place(x=295,y=250)
    zoneDrop7.place(x=345,y=250)
    zoneDrop8.place(x=395,y=250)
    fonction=2
    creation_mot()
def sept():
    global fonction
    label_drop()
    choix1.place(x=30,y=50)
    choix2.place(x=80,y=50)
    choix3.place(x=130,y=50)
    choix4.place(x=180,y=50)
    choix5.place(x=230,y=50)
    choix6.place(x=280,y=50)
    choix7.place(x=330,y=50)
    choix8.place(x=380,y=50)
    choix9.place(x=430,y=50)
    zoneDrop1.place(x=65,y=250)
    zoneDrop2.place(x=115,y=250)
    zoneDrop3.place(x=165,y=250)
    zoneDrop4.place(x=215,y=250)
    zoneDrop5.place(x=265,y=250)
    zoneDrop6.place(x=315,y=250)
    zoneDrop7.place(x=365,y=250)
    fonction=3
    creation_mot()

def six():
    global fonction
    label_drop()
    choix1.place(x=30,y=50)
    choix2.place(x=80,y=50)
    choix3.place(x=130,y=50)
    choix4.place(x=180,y=50)
    choix5.place(x=230,y=50)
    choix6.place(x=280,y=50)
    choix7.place(x=330,y=50)
    choix8.place(x=380,y=50)
    choix9.place(x=430,y=50)
    zoneDrop1.place(x=85,y=250)
    zoneDrop2.place(x=135,y=250)
    zoneDrop3.place(x=185,y=250)
    zoneDrop4.place(x=235,y=250)
    zoneDrop5.place(x=285,y=250)
    zoneDrop6.place(x=335,y=250)
    fonction=4
    creation_mot()

def cinq():
    global fonction
    label_drop()
    choix1.place(x=30,y=50)
    choix2.place(x=80,y=50)
    choix3.place(x=130,y=50)
    choix4.place(x=180,y=50)
    choix5.place(x=230,y=50)
    choix6.place(x=280,y=50)
    choix7.place(x=330,y=50)
    choix8.place(x=380,y=50)
    choix9.place(x=430,y=50)
    zoneDrop1.place(x=115,y=250)
    zoneDrop2.place(x=165,y=250)
    zoneDrop3.place(x=215,y=250)
    zoneDrop4.place(x=265,y=250)
    zoneDrop5.place(x=315,y=250)
    fonction=5
    creation_mot()

def quatre():
    global fonction
    label_drop()
    choix1.place(x=30,y=50)
    choix2.place(x=80,y=50)
    choix3.place(x=130,y=50)
    choix4.place(x=180,y=50)
    choix5.place(x=230,y=50)
    choix6.place(x=280,y=50)
    choix7.place(x=330,y=50)
    choix8.place(x=380,y=50)
    choix9.place(x=430,y=50)
    zoneDrop1.place(x=135,y=250)
    zoneDrop2.place(x=185,y=250)
    zoneDrop3.place(x=235,y=250)
    zoneDrop4.place(x=285,y=250)
    fonction=6
    creation_mot()

def trois():
    global fonction
    label_drop()
    choix1.place(x=30,y=50)
    choix2.place(x=80,y=50)
    choix3.place(x=130,y=50)
    choix4.place(x=180,y=50)
    choix5.place(x=230,y=50)
    choix6.place(x=280,y=50)
    choix7.place(x=330,y=50)
    choix8.place(x=380,y=50)
    choix9.place(x=430,y=50)
    zoneDrop1.place(x=175,y=250)
    zoneDrop2.place(x=225,y=250)
    zoneDrop3.place(x=275,y=250)
    fonction=7
    creation_mot()

def deux():
    global fonction
    creation_mot()
    label_drop()
    choix1.place(x=30,y=50)
    choix2.place(x=80,y=50)
    choix3.place(x=130,y=50)
    choix4.place(x=180,y=50)
    choix5.place(x=230,y=50)
    choix6.place(x=280,y=50)
    choix7.place(x=330,y=50)
    choix8.place(x=380,y=50)
    choix9.place(x=430,y=50)
    zoneDrop1.place(x=200,y=250)
    zoneDrop2.place(x=275,y=250)
    fonction=8

def un():
    global fonction
    creation_mot()
    label_drop()
    choix1.place(x=30,y=50)
    choix2.place(x=80,y=50)
    choix3.place(x=130,y=50)
    choix4.place(x=180,y=50)
    choix5.place(x=230,y=50)
    choix6.place(x=280,y=50)
    choix7.place(x=330,y=50)
    choix8.place(x=380,y=50)
    choix9.place(x=430,y=50)
    zoneDrop1.place(x=230,y=250)
    fonction=9

#création des label de choix
def drag():
    global choix1,choix2,choix3,choix4,choix5,choix6,choix7,choix8,choix9,liste
    choix1 = Label(crea, text=liste[0],fg="yellow", bg="black",font=("Helvetica", 20),height = 2, width=3)
    choix2 = Label(crea, text=liste[1],fg="yellow", bg="black",font=("Helvetica", 20),height = 2, width=3)
    choix3 = Label(crea, text=liste[2],fg="yellow", bg="black",font=("Helvetica", 20),height = 2, width=3)
    choix4 = Label(crea, text=liste[3],fg="yellow", bg="black",font=("Helvetica", 20),height = 2, width=3)
    choix5 = Label(crea, text=liste[4],fg="yellow", bg="black",font=("Helvetica", 20),height = 2, width=3)
    choix6 = Label(crea, text=liste[5],fg="yellow", bg="black",font=("Helvetica", 20),height = 2, width=3)
    choix7 = Label(crea, text=liste[6],fg="yellow", bg="black",font=("Helvetica", 20),height = 2, width=3)
    choix8 = Label(crea, text=liste[7],fg="yellow", bg="black",font=("Helvetica", 20),height = 2, width=3)
    choix9 = Label(crea, text=liste[8],fg="yellow", bg="black",font=("Helvetica", 20),height = 2, width=3)
    drag1 = DragManager(choix1,drag=True,drop=False)
    drag2 = DragManager(choix2,drag=True,drop=False)
    drag3 = DragManager(choix3,drag=True,drop=False)
    drag4 = DragManager(choix4,drag=True,drop=False)
    drag5 = DragManager(choix5,drag=True,drop=False)
    drag6 = DragManager(choix6,drag=True,drop=False)
    drag7 = DragManager(choix7,drag=True,drop=False)
    drag8 = DragManager(choix8,drag=True,drop=False)
    drag9 = DragManager(choix9,drag=True,drop=False)

#fonction pour creer le mode de jeu sprint
def sprint():
    global duree,mode_jeu
    duree=50
    mode.withdraw()
    mode_jeu="sprint"
    selection()
    

#fonction pour creer le mode de jeu marathon
def marathon():
    global duree,mode_jeu
    duree=300
    mode.withdraw()
    mode_jeu="marathon"
    selection()
    
#fonction pour choisir les lettres
def selection():
    global compteur_consonnes, compteur_lettres,label_erreur1,crea,neuf1,huit1,sept1,six1,cinq1,quatre1,trois1,deux1,un1,liste,text_timer,btn_recommencer,arreter
    accueil.withdraw()
    select.deiconify()
    #parametre de la page select
    select.title("Jeu")
    select.geometry("500x500+400+100")
    select.config(bg = couleur)
    #création des buttons
    retour = customtkinter.CTkButton(select, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)
    retour.place(x= 10, y=5)
    quitter = customtkinter.CTkButton(select,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=440,y=5)
    btn_recommencer = Button(select, bg="#D5C935", text="Recommencer", command=recommencer)
    btn_recommencer.place(x=200, y =470)   
    arreter=Button(select,text="Arreter",bg="#D5C935",command=stop)
    if mode_jeu=="marathon":
        btn_recommencer.place(x=260,y=470)
        arreter.place(x=200,y=470)
    #fonction du timer pour le mode marathon
    def Timer1():
        global duree
        if duree > 0:
            text_timer["text"] = str(duree) + "s"
            duree -= 1
            select.after(1000, Timer1)  #mise à jour chaque secondes
        elif duree==0:
            if mode_jeu=="marathon":
                final()           
            if mode_jeu=="sprint":
                Label(crea,text="Vous n'avez plus de temps",bg="red").place(x=100,y=260)
                time.sleep(2)
                final()
    #label affichage du timer
    text_timer=Label(select,text="",bg=couleur,font=(12))
    text_timer.place(x=240,y=400)

    Timer1()
    #fonction pour désactiver les bouton à chaque initialisation de la page
    def desactiver_bouton():
        neuf1.config(state="disabled",text="sélectionner\n d'abord\nles lettres")
        huit1.config(state="disabled",text="sélectionner\n d'abord\nles lettres")
        sept1.config(state="disabled",text="sélectionner\n d'abord\nles lettres")
        six1.config(state="disabled",text="sélectionner\n d'abord\nles lettres")
        cinq1.config(state="disabled",text="sélectionner\n d'abord\nles lettres")
        quatre1.config(state="disabled",text="sélectionner\n d'abord\nles lettres")
        trois1.config(state="disabled",text="sélectionner\n d'abord\nles lettres")
        deux1.config(state="disabled",text="sélectionner\n d'abord\nles lettres")
        un1.config(state="disabled",text="sélectionner\n d'abord\nles lettres")
    #label des consignes
    zone_texte = Label (select,text = "cliquer sur le nombre de lettres que va contenir votre mot",bg=couleur )
    zone_texte2 = Label (select,text = "Choisisser entre une consonne ou une voyelle",bg=couleur )
    zone_texte2.place(x=120, y=440)
    label_erreur1 = Label(select, text="Vous ne pouvez sélectionner que 6 consonnes maximum", bg="red")

    #liste et variable
    consonnes = ["r"] * 60 + ["s"] * 60 + ["n"] * 50 + ["t"] * 50 + ["l"] * 50 + ["d"] * 40 + ["c"] * 30 + ["p"] * 30 + ["m"] * 30 + ["v"] * 20 + ["q"] * 10 + ["f"] * 10 + ["b"] * 10 + ["g"] * 10 + ["h"] * 10 + ["j"] * 3 + ["x"] * 3 + ["z"] * 1 + ["k"] * 1 + ["w"] * 1
    voyelles = ["a"] * 12 + ["e"] * 14 + ["i"] * 8 + ["o"] * 8 + ["u"] * 7 + ["y"] * 1
    compteur_consonnes=0
    compteur_lettres=0

    def consonne():#Configuration du bouton consonne
        global compteur_consonnes, compteur_lettres, label_erreur1,liste
        #selection de consonnes
        if compteur_consonnes<6:
            liste.append(consonnes[randint(0,len(consonnes)-1)])
            compteur_consonnes+=1
            compteur_lettres+=1
            lettres()
        #seuelemtn 6 consonnes selectionnable
        elif compteur_consonnes>=6:
            consonne.config(state="disabled")
            label_erreur1.place(x=60,y=240)
        #bouton désactiver tant que 9 lettres non pas été selectionner
        if compteur_lettres>8:
            consonne.config(state="disabled")
            voyelle.config(state="disabled")
            zone_texte2.destroy()
            zone_texte.place(x=100,y=240)
            label_erreur2 = Label(select, text="Vous avez atteint le nombre de lettres maximum", bg="red")
            label_erreur2.place(x=120,y=320)
            neuf1.config(state="normal",text="9")
            huit1.config(state="normal",text="8")
            sept1.config(state="normal",text="7")
            six1.config(state="normal",text="6")
            cinq1.config(state="normal",text="5")
            quatre1.config(state="normal",text="4")
            trois1.config(state="normal",text="3")
            deux1.config(state="normal",text="2")
            un1.config(state="normal",text="1")
            drag()
    def voyelle():#Configuration Bouton voyelle
        global compteur_lettres,liste
        label_erreur1.destroy()
        #selection de lettre
        liste.append(voyelles[randint(0,len(voyelles)-1)])
        lettres()
        compteur_lettres+=1
        #bouton désactiver tant que 9 lettres non pas été selectionner
        if compteur_lettres>8:
            voyelle.config(state="disabled")
            consonne.config(state="disabled")
            zone_texte2.destroy()
            zone_texte.place(x=100,y=240)
            label_erreur2 = Label(select, text="Vous avez atteint le nombre de lettres maximum", bg="red")
            label_erreur2.place(x=120,y=320)
            neuf1.config(state="normal",text="9")
            huit1.config(state="normal",text="8")
            sept1.config(state="normal",text="7")
            six1.config(state="normal",text="6")
            cinq1.config(state="normal",text="5")
            quatre1.config(state="normal",text="4")
            trois1.config(state="normal",text="3")
            deux1.config(state="normal",text="2")
            un1.config(state="normal",text="1")
            drag()
    #fonction d'appariton des lettres
    def lettres():
        global liste_label
        label_lettre = Label(select, text=liste, font=("Courier",30),bg=couleur)
        label_lettre.place(x=40, y=270)
        liste_label.append(label_lettre)

    #Bouton nombre de lettres du mots
    neuf1=Button(select, text="9",heigh=5,width=10, bg="#E3DE6C", command=neuf)
    neuf1.place(x=25,y=30)
    huit1=Button(select, text="8",heigh=5,width=10, bg="#E3DE6C", command=huit)
    huit1.place(x=115,y=30)
    sept1=Button(select, text="7",heigh=5,width=10, bg="#E3DE6C", command=sept)
    sept1.place(x=205,y=30)
    six1=Button(select, text="6",heigh=5,width=10, bg="#E3DE6C", command=six)
    six1.place(x=295,y=30)
    cinq1=Button(select, text="5",heigh=5,width=10, bg="#E3DE6C", command=cinq)
    cinq1.place(x=385,y=30)
    quatre1=Button(select, text="4",heigh=5,width=10, bg="#E3DE6C", command=quatre)
    quatre1.place(x=50,y=130)
    trois1=Button(select, text="3",heigh=5,width=10, bg="#E3DE6C", command=trois)
    trois1.place(x=150,y=130)
    deux1=Button(select, text="2",heigh=5,width=10, bg="#E3DE6C", command=deux)
    deux1.place(x=250,y=130)
    un1=Button(select, text="1",heigh=5,width=10, bg="#E3DE6C", command=un)
    un1.place(x=350,y=130)
    desactiver_bouton()

    #Bouton selection lettres
    voyelle=Button(select, text="voyelle",heigh=5,width=20, bg="#DCD546", command=voyelle)
    voyelle.place(x=50,y=350)
    consonne=Button(select, text="consonne",heigh=5,width=20, bg="#DCD546", command=consonne)
    consonne.place(x=300,y=350)

def mod():
    accueil.withdraw()
    mode.deiconify()
    mode.geometry("500x500+400+100")
    mode.title('Choisir le mode de jeu')
    mode.config(bg=couleur)
    Label(mode,text="Choisissez votre mode de jeu",bg=couleur,font=("Arial",14,"bold")).place(x=100,y=70)
    btn_Sprint = customtkinter.CTkButton(mode,text='Sprint',height=150, width=180,fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",border_width=1,border_color='black', command=sprint)
    btn_Sprint.place(x=260, y=230)
    btn_marathon = customtkinter.CTkButton(mode,text="Marathon",height=150, width=180,fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",border_width=1,border_color='black', command=marathon)
    btn_marathon.place(x=60, y=230)
    retour = customtkinter.CTkButton(mode, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)
    retour.place(x= 10, y=5)
    quitter = customtkinter.CTkButton(mode,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=440,y=5)
    
    
def pg_achivement():
    accueil.withdraw()
    objectif2.withdraw()
    objectif.deiconify()
    objectif.geometry("500x500+400+100")
    objectif.title('Achivement')
    objectif.config(bg=couleur)
    if 'temps_debut' in globals():
        temps_fin = time.time()
        for chemin in chemins:
                if os.path.exists(chemin):
                    with open(chemin, mode="r", newline='') as fichier_csv:
                        lecteur_csv = csv.DictReader(fichier_csv)
                        donnees = list(lecteur_csv)
        for ligne in donnees:
            if ligne["Pseudo"]==username:
                ligne["dernier_temps"] = int(temps_fin - temps_debut)
        for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="w", newline='') as fichier_csv:
                    noms_colonnes = ["Pseudo", "Mdp","total_sprint","total_marathon","ach1","ach2", "ach3","ach4","ach5","ach6","ach7","ach8","ach9","ach10","ach11","ach12","ach13","ach14","ach15","ach16","nb_partie_sprint","nb_partie_marathon","9","8","7","6","5","4","3","2","1","Score_sprint","Score_mara","nb_mot_marathon","dernier_temps"]               
                    ecrivain = csv.DictWriter(fichier_csv, fieldnames=noms_colonnes)
                    ecrivain.writeheader()
                    ecrivain.writerows(donnees)
    def achivement():
            for chemin in chemins:
                if os.path.exists(chemin):
                    with open(chemin, mode="r", newline='') as fichier_csv:
                        lecteur_csv = csv.DictReader(fichier_csv)
                        donnees = list(lecteur_csv)
            for ligne in donnees:
                if ligne["Pseudo"]==username:
                    if ligne["ach1"]=="Oui":
                        ach1.config(text="Vous avez réussie\n à obtenir\n 100pts en une partie",bg="#48EF13")
                    if ligne["ach2"]=="Oui":
                        ach2.config(text="Vous avez réussie\n à avoir\n 200pts au total", bg="#48EF13")
                    if ligne["ach3"]=="Oui":
                        ach3.config(text="Vous avez réussie\n à avoir\n 300pts au total", bg="#48EF13")
                    if ligne["ach4"]=="Oui":
                        ach4.config(text="Vous avez réussie\n à avoir\n 400pts au total", bg="#48EF13")
                    if ligne["ach5"]=="Oui":
                        ach5.config(text="Vous avez réussie\n à avoir\n 500pts au total", bg="#48EF13")
                    if ligne["ach6"]=="Oui":
                        ach6.config(text="Vous avez réussie\n à avoir\n 600pts au total", bg="#48EF13")
                    if ligne["ach7"]=="Oui":
                        ach7.config(text="Vous avez réussie\n à avoir\n 700pts au total", bg="#48EF13")
                    if ligne["ach8"]=="Oui":
                        ach8.config(text="Vous avez réussie\n à avoir\n 800pts au total", bg="#48EF13")
                    if ligne["ach9"]=="Oui":
                        ach9.config(text="Vous avez réussie\n à avoir\n 900pts au total", bg="#48EF13")
                    if ligne["ach10"]=="Oui":
                        ach10.config(text="Vous avez réussie\n à avoir\n 1000pts au total", bg="#48EF13")
                    if ligne["ach11"]=="Oui":
                        ach11.config(text="Vous avez réussie\n à avoir\n 800pts dans le mode\nmarathon", bg="#48EF13")
                    if ligne["ach11"]=="Oui":
                        ach12.config(text="Vous avez réussie\n à avoir\n 1000pts dans le mode\nmarathon", bg="#48EF13")
    def modif():
        for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="r", newline='') as fichier_csv:
                    lecteur_csv = csv.DictReader(fichier_csv)
                    donnees = list(lecteur_csv)
        for ligne in donnees:
            if ligne["Pseudo"]==username and ligne["total_sprint"] is not None and ligne["total_sprint"] != '':
                if float(ligne["Score_sprint"])==150:
                    ligne["ach1"]="Oui"
                if int(ligne["Score_mara"])>=800:
                    ligne["ach11"]='Oui'
                    if int(ligne["Score_mara"])>=1000:
                        ligne["ach12"]='Oui'
                if float(ligne["total_sprint"])>=200:
                    ligne["ach2"]="Oui"
                    if float(ligne["total_sprint"])>=300:
                        ligne["ach3"]="Oui"
                        if float(ligne["total_sprint"])>=400:
                            ligne["ach4"]="Oui"
                            if float(ligne["total_sprint"])>=500:
                                ligne["ach5"]="Oui"
                                if float(ligne["total_sprint"])>=600:
                                    ligne["ach6"]="Oui"
                                    if float(ligne["total_sprint"])>=600:
                                        ligne["ach7"]="Oui"
                                        if float(ligne["total_sprint"])>=800:
                                            ligne["ach8"]="Oui"
                                            if float(ligne["total_sprint"])>=900:
                                                ligne["ach9"]="Oui"
                                                if float(ligne["total_sprint"])>=1000:
                                                    ligne["ach10"]="Oui"
        fichier_csv.close()
        for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="w", newline='') as fichier_csv:
                    noms_colonnes = ["Pseudo", "Mdp","total_sprint","total_marathon","ach1","ach2", "ach3","ach4","ach5","ach6","ach7","ach8","ach9","ach10","ach11","ach12","ach13","ach14","ach15","ach16","nb_partie_sprint","nb_partie_marathon","9","8","7","6","5","4","3","2","1","Score_sprint","Score_mara","nb_mot_marathon","dernier_temps"]               
                    ecrivain = csv.DictWriter(fichier_csv, fieldnames=noms_colonnes)                
                    ecrivain.writeheader()
                    ecrivain.writerows(donnees)
        fichier_csv.close()

    ach1=Label(objectif, text="Pour débloquer cette \nachivement il faut \nréussir à obtenir \n150pts en une partie\n de sprint",height=7, width=16, bg="#7A7676")
    ach1.place(x=10,y=30)
    ach2=Label(objectif, text="Pour débloquer cette \nachivement il faut \navoir 200pts au total\nen mode sprint",height=7, width=16, bg="#7A7676")
    ach2.place(x=130,y=30)
    ach3=Label(objectif, text="Pour débloquer cette \nachivement il faut \navoir 300pts au total\nen mode sprint",height=7, width=16, bg="#7A7676")
    ach3.place(x=250,y=30)
    ach4=Label(objectif, text="Pour débloquer cette \nachivement il faut \navoir 400pts au total\nen mode sprint",height=7, width=16, bg="#7A7676")
    ach4.place(x=370,y=30)
    ach5=Label(objectif, text="Pour débloquer cette \nachivement il faut \navoir 500pts au total\nen mode sprint",height=7, width=16, bg="#7A7676")
    ach5.place(x=10,y=180)
    ach6=Label(objectif, text="Pour débloquer cette \nachivement il faut \navoir 600pts au total\nen mode sprint",height=7, width=16, bg="#7A7676")
    ach6.place(x=130,y=180)
    ach7=Label(objectif, text="Pour débloquer cette \nachivement il faut \navoir 700pts au total\nen mode sprint",height=7, width=16, bg="#7A7676")
    ach7.place(x=250,y=180)
    ach8=Label(objectif, text="Pour débloquer cette \nachivement il faut \navoir 800pts au total\nen mode sprint",height=7, width=16, bg="#7A7676")
    ach8.place(x=370,y=180)
    ach9=Label(objectif, text="Pour débloquer cette \nachivement il faut \navoir 900pts au total\nen mode sprint",height=7, width=16, bg="#7A7676")
    ach9.place(x=10,y=330)
    ach10=Label(objectif, text="Pour débloquer cette \nachivement il faut \navoir 1000pts au total\nen mode sprint",height=7, width=16, bg="#7A7676")
    ach10.place(x=130,y=330)
    ach11=Label(objectif, text="Pour débloquer cette \nachivement il faut \nréussir à obtenir \n1000pts\n \nen mode marathon",height=7, width=16, bg="#7A7676")
    ach11.place(x=370,y=330)
    ach12=Label(objectif, text="Pour débloquer cette \nachivement il faut \nréussir à obtenir \n800pts\n \nen mode marathon",height=7, width=16, bg="#7A7676")
    ach12.place(x=250,y=330)
    modif()
    achivement()
    Titre=Label(objectif,text="Vos Achivement",bg=couleur,fg='red',font=("Arial",12,'bold'))
    Titre.place(x=210,y=0)
    retour = customtkinter.CTkButton(objectif, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)
    retour.place(x= 10, y=5)
    quitter = customtkinter.CTkButton(objectif,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=440,y=5)
    page=customtkinter.CTkButton(objectif,text="Page suivante",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black',command=pg_achivement2)
    page.place(x=405,y=470)

def pg_achivement2():
    accueil.withdraw()
    objectif.withdraw()
    objectif2.deiconify()
    objectif2.geometry("500x500+400+100")
    objectif2.title('Achivement')
    objectif2.config(bg=couleur)
    if 'temps_debut' in globals():
        temps_fin = time.time()
        for chemin in chemins:
                if os.path.exists(chemin):
                    with open(chemin, mode="r", newline='') as fichier_csv:
                        lecteur_csv = csv.DictReader(fichier_csv)
                        donnees = list(lecteur_csv)
        for ligne in donnees:
            if ligne["Pseudo"]==username:
                ligne["dernier_temps"] = int(temps_fin - temps_debut)
        for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="w", newline='') as fichier_csv:
                    noms_colonnes = ["Pseudo", "Mdp","total_sprint","total_marathon","ach1","ach2", "ach3","ach4","ach5","ach6","ach7","ach8","ach9","ach10","ach11","ach12","ach13","ach14","ach15","ach16","nb_partie_sprint","nb_partie_marathon","9","8","7","6","5","4","3","2","1","Score_sprint","Score_mara","nb_mot_marathon","dernier_temps"]               
                    ecrivain = csv.DictWriter(fichier_csv, fieldnames=noms_colonnes)
                    ecrivain.writeheader()
                    ecrivain.writerows(donnees)

    ach13=Label(objectif2, text="Pour débloquer cet \nachievement, il faut \navoir joué pendant 1H",height=7, width=16, bg="#7A7676")
    ach13.place(x=10,y=30)
    ach14=Label(objectif2, text="Pour débloquer cet \nachivement il faut \navoir joué 5h",height=7, width=16, bg="#7A7676")
    ach14.place(x=130,y=30)
    ach15=Label(objectif2, text="Pour débloquer cet \nachivement il faut \navoir joué 10H",height=7, width=16, bg="#7A7676")
    ach15.place(x=250,y=30)
    ach16=Label(objectif2, text="Pour débloquer cet \nachivement il faut \navoir joué 100H",height=7, width=16, bg="#7A7676")
    ach16.place(x=370,y=30)
    for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="r", newline='') as fichier_csv:
                    lecteur_csv = csv.DictReader(fichier_csv)
                    donnees = list(lecteur_csv)
    for ligne in donnees:
        if ligne["Pseudo"]==username:
            if int(ligne["dernier_temps"])>=3600:
                ach13.config(text="Vous avez joué\nplus de 1H",bg="#48EF13")
                ligne["ach13"]="Oui"
                if int(ligne["dernier_temps"])>=18000:
                    ach14.config(text="Vous avez joué\n plus de 5H",bg="#48EF13")
                    ligne["ach14"]="Oui"
                    if int(ligne["dernier_temps"])>=36000:
                        ach15.config(text="Vous avez joué\n plus de 10H",bg="#48EF13")
                        ligne["ach15"]="Oui"
                        if int(ligne["dernier_temps"])>=360000: 
                            ach16.config(text="Vous avez joué\n plus de 100H",bg="#48EF13")
                            ligne["ach16"]='Oui'
    for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="w", newline='') as fichier_csv:
                    noms_colonnes = ["Pseudo", "Mdp","total_sprint","total_marathon","ach1","ach2", "ach3","ach4","ach5","ach6","ach7","ach8","ach9","ach10","ach11","ach12","ach13","ach14","ach15","ach16","nb_partie_sprint","nb_partie_marathon","9","8","7","6","5","4","3","2","1","Score_sprint","Score_mara","nb_mot_marathon","dernier_temps"]               
                    ecrivain = csv.DictWriter(fichier_csv, fieldnames=noms_colonnes)                
                    ecrivain.writeheader()
                    ecrivain.writerows(donnees)
            fichier_csv.close()

    Titre=Label(objectif2,text="Vos Achivements",bg=couleur,fg='red',font=("Arial",12,'bold'))
    Titre.place(x=210,y=0)
    retour = customtkinter.CTkButton(objectif2, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)
    retour.place(x= 10, y=5)
    quitter = customtkinter.CTkButton(objectif2,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=440,y=5)
    page=customtkinter.CTkButton(objectif2,text="Page précédente",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black',command=pg_achivement)
    page.place(x=10,y=470)

def fond():
    accueil.withdraw()
    color.deiconify()
    color.geometry("500x500+400+100")
    color.title("Fond")
    background=couleur
    color.config(bg=background)
    def bg():
        global verif_fond,start
        def brown():
            global couleur
            couleur="#FFE4B5"
            color.config(bg=couleur)
            bg()
        def black():
            global couleur
            couleur="#40403D"
            color.config(bg=couleur)
            bg()
        def vert():
            global couleur
            couleur="#10AC21"
            color.config(bg=couleur)
            bg()
        def yellow():
            global couleur
            couleur="#F1C40F"
            color.config(bg=couleur)
            bg()
        def Orange():
            global couleur
            couleur="#EC941D"
            color.config(bg=couleur)
            bg()
        def purple():
            global couleur
            couleur="#512E5F"
            color.config(bg=couleur)
            bg()
        def blue():
            global couleur
            couleur="#1B4F72"
            color.config(bg=couleur)
            bg()
        def Cyan():
            global couleur
            couleur="#0E6251"
            color.config(bg=couleur)
            bg()
        def red():
            global couleur
            couleur="#7B241C"
            color.config(bg=couleur)
            bg()
    
        Titre=Label(color, text="Vous pouvez choisir un nouveau fond", bg=couleur)
        Titre.place(x=150,y=10)
        def start():
            global noir,green,marron,jaune,orange,violet,bleu,cyan,rouge
            noir=Button(color,text="Couleur déblocable à\n partir de 800 pts",bg="#50504D",fg="White",height=8,width=18,relief="sunken",command=black)
            noir.place(x=350,y=50)
            green=Button(color,text="Couleur déblocable à\n partir de 300 pts",bg="#13B925",fg="Black",height=8,width=18,relief="sunken",command=vert)
            green.place(x=184, y=50)
            marron=Button(color,text="Beige",bg="#FFE8C0",fg="Black",height=8,width=18,command=brown,relief="sunken")
            marron.place(x=15, y=50)
            jaune=Button(color,text="Couleur déblocable à\n partir de 1000 pts",bg="#F4D03F",fg="Black",height=8,width=18,relief="sunken",command=yellow)
            jaune.place(x=15,y=200)
            orange=Button(color,text="Couleur déblocable à \n partir de 2000 pts",bg="#FF9300",fg="Black",height=8,width=18,relief="sunken",command=Orange)
            orange.place(x=184, y=200)
            violet=Button(color,text="Couleur déblocable à\n partir de 3000 pts",bg="#76448A",fg="Black",height=8,width=18,command=purple,relief="sunken")
            violet.place(x=350, y=200)
            bleu=Button(color,text="Couleur déblocable à\n partir de 5000 pts",bg="#2874A6",fg="Black",height=8,width=18,relief="sunken",command=blue)
            bleu.place(x=15,y=350)
            cyan=Button(color,text="Couleur déblocable à\n partir de 8000 pts",bg="#148F77",fg="Black",height=8,width=18,relief="sunken",command=Cyan)
            cyan.place(x=184, y=350)
            rouge=Button(color,text="Couleur déblocable à\n partir de 10000 pts",bg="#A93226",fg="Black",height=8,width=18,command=red,relief="sunken")
            rouge.place(x=350, y=350)
            noir.config(state="disabled")
            green.config(state="disabled")
            rouge.config(state="disabled")
            cyan.config(state="disabled")
            bleu.config(state="disabled")
            violet.config(state="disabled")
            orange.config(state="disabled")
            jaune.config(state="disabled")
    
        def verif_fond():
            for chemin in chemins:
                if os.path.exists(chemin):
                    with open(chemin, mode="r", newline='') as fichier_csv:
                        lecteur_csv = csv.DictReader(fichier_csv)
                        donnees = list(lecteur_csv)
            for ligne in donnees:
                if ligne["Pseudo"] == username and ligne["total_sprint"] is not None and ligne["total_sprint"] != '':
                    if int(ligne["total_sprint"])+int(ligne["total_marathon"])>=300:
                        green.config(state=("normal"))
                        green.config(text="Vert")
                        if int(ligne["total_sprint"])+int(ligne["total_marathon"])>=800:
                            noir.config(state=("normal"))
                            noir.config(text="Noir")
                            if int(ligne["total_sprint"])+int(ligne["total_marathon"])>=1000:
                                jaune.config(state=("normal"))
                                jaune.config(text="Jaune")
                                if int(ligne["total_sprint"])+int(ligne["total_marathon"])>=2000:
                                    orange.config(state=("normal"))
                                    orange.config(text="Orange")
                                    if int(ligne["total_sprint"])+int(ligne["total_marathon"])>=3000:
                                            violet.config(state=("normal"))
                                            violet.config(text=("Violet"))
                                            if int(ligne["total_sprint"])+int(ligne["total_marathon"])>=5000:
                                                bleu.config(state=("normal"))
                                                bleu.config(text="Bleu")
                                                if int(ligne["total_sprint"])+int(ligne["total_marathon"])>=8000:
                                                    cyan.config(state=("normal"))
                                                    cyan.config(text="Cyan")
                                                    if int(ligne["total_sprint"])+int(ligne["total_marathon"])>=10000:
                                                        rouge.config(state=("normal"))
                                                        rouge.config(text="Rouge")
            for chemin in chemins:
                if os.path.exists(chemin):
                    with open(chemin, mode="w", newline='') as fichier_csv:
                        noms_colonnes = ["Pseudo", "Mdp","total_sprint","total_marathon","ach1","ach2", "ach3","ach4","ach5","ach6","ach7","ach8","ach9","ach10","ach11","ach12","ach13","ach14","ach15","ach16","nb_partie_sprint","nb_partie_marathon","9","8","7","6","5","4","3","2","1","Score_sprint","Score_mara","nb_mot_marathon","dernier_temps"]               
                        ecrivain = csv.DictWriter(fichier_csv, fieldnames=noms_colonnes)
                        ecrivain.writeheader()
                        ecrivain.writerows(donnees)            
    bg()
    start()
    verif_fond()
    retour = customtkinter.CTkButton(color, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)#creation du bouton de retour à l'accueil
    retour.place(x= 10, y=10)
    quitter = customtkinter.CTkButton(color,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=440,y=10)

def rank():
    accueil.withdraw()
    best2.withdraw()
    best.deiconify()
    best.title("Classement")
    best.geometry("430x300+400+100")
    best.config(bg=couleur)
    classement1=0
    classement2=0
    y=80
    y2=80

    def trier_total_point():
        for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="r", newline='') as fichier_csv:
                    lecteur_csv = csv.DictReader(fichier_csv)
                    donnees = list(lecteur_csv)
        #Filtre les lignes pour ne conserver que celles avec des valeurs numériques dans la colonne 3
        donnees_filtrees = [ligne for ligne in donnees if ligne["total_sprint"] is not None and ligne["total_sprint"].isdigit()]
        #Trie la liste de tuples par rapport à la colonne 3
        donnees_triees = sorted(donnees_filtrees, key=lambda x: int(x["total_sprint"])+int(x['total_marathon']), reverse=True)
        return donnees_triees
    
    def trier_max_point_sprint():
        for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="r", newline='') as fichier_csv:
                    lecteur_csv = csv.DictReader(fichier_csv)
                    donnees = list(lecteur_csv)
        #Filtre les lignes pour ne conserver que celles avec des valeurs numériques dans la colonne 3
        donnees_filtrees = [ligne for ligne in donnees if ligne["Score_sprint"] is not None]
        #Trie la liste de tuples par rapport à la colonne 3
        donnees_triees = sorted(donnees_filtrees, key=lambda x: float(x["Score_sprint"]), reverse=True)
        return donnees_triees
    
    #Lecture et tri des données du fichier CSV
    donnees1 = trier_total_point()
    donnees2 = trier_max_point_sprint()
    Titre1 = Label(best, text="Classement des personnes avec\n le plus de points:",font=('Aldus', 9,"bold"),fg="Red", bg=couleur)
    Titre1.place(x=0,y=40)
    Titre2 = Label(best, text="Classement des personnes avec\n le plus haut score en mode Sprint:",font=('Aldus', 9,"bold"),fg="Red", bg=couleur)
    Titre2.place(x=210,y=40)
    for ligne in donnees1:
        classement1+=1
        # Affichage des données de la colonne 1 et 3 pour chaque ligne
        texte_ligne1 = f"{classement1}:  Pseudo: {ligne['Pseudo']}"
        texte_ligne2 = f"Score: {str(int(ligne['total_sprint'])+int(ligne["total_marathon"]))}"
        Label(best, text=texte_ligne1,font=('Aldus', 9), bg=couleur).place(x=10,y=y)
        Label(best, text=texte_ligne2,font=('Aldus', 9), bg=couleur).place(x=110,y=y)
        y+=25
    for ligne in donnees2:
        classement2+=1
        # Affichage des données de la colonne 1 et 3 pour chaque ligne
        texte_ligne1 = f"{classement2}:  Pseudo: {ligne['Pseudo']}"
        texte_ligne2 = f"Score: {ligne['Score_sprint']}"
        Label(best, text=texte_ligne1,font=('Aldus', 9), bg=couleur).place(x=220,y=y2)
        Label(best, text=texte_ligne2,font=('Aldus', 9), bg=couleur).place(x=320,y=y2)
        y2+=25
    retour = customtkinter.CTkButton(best, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)
    retour.place(x= 10, y=10)
    quitter = customtkinter.CTkButton(best,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=330,y=10)
    page=customtkinter.CTkButton(best,text="Page suivante",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black',command=rank2)
    page.place(x=300,y=270)

def rank2():
    best.withdraw()
    best2.deiconify()
    best2.title("Classement")
    best2.geometry("400x300+400+100")
    best2.config(bg=couleur)
    classement3=0
    y3=80
    def trier_max_point_marathon():
        for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="r", newline='') as fichier_csv:
                    lecteur_csv = csv.DictReader(fichier_csv)
                    donnees = list(lecteur_csv)
        #Filtre les lignes pour ne conserver que celles avec des valeurs numériques dans la colonne 3
        donnees_filtrees = [ligne for ligne in donnees if ligne["Score_mara"] is not None and ligne["Score_mara"].isdigit()]
        #Trie la liste de tuples par rapport à la colonne 3
        donnees_triees = sorted(donnees_filtrees, key=lambda x: int(x["Score_mara"]), reverse=True)
        return donnees_triees
    donnees3 = trier_max_point_marathon()
    Titre3 = Label(best2, text="Classement des personnes avec\n le plus haut score en mode marathon:",font=('Aldus', 12,"bold"),fg="Red", bg=couleur)
    Titre3.place(x=80,y=40)
    for ligne in donnees3:
        classement3+=1
        # Affichage des données de la colonne 1 et 3 pour chaque ligne
        texte_ligne1 = f"{classement3}:  Pseudo: {ligne['Pseudo']}"
        texte_ligne2 = f"Score: {ligne['Score_mara']}"
        Label(best2, text=texte_ligne1,font=('Aldus', 9), bg=couleur).place(x=100,y=y3)
        Label(best2, text=texte_ligne2,font=('Aldus', 9), bg=couleur).place(x=250,y=y3)
        y3+=25
    retour = customtkinter.CTkButton(best2, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)
    retour.place(x= 10, y=10)
    quitter = customtkinter.CTkButton(best2,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=330,y=10)
    page=customtkinter.CTkButton(best2,text="Page précédente",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black',command=rank)
    page.place(x=10,y=270)


def point(username, valeur):
    #Ouvre le fichier CSV en mode lecture
    with open("./compte.csv", mode="r", newline='') as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv)
        lignes = list(lecteur_csv)
    #modifie la valeur de total_sprint dans le csv
    if mode_jeu=="sprint":
        for ligne in lignes:
            if ligne["Pseudo"] == username:
                if ligne["total_sprint"] is not None and ligne["total_sprint"] != '':
                    ligne["total_sprint"] = int(ligne["total_sprint"]) + int(valeur) #Modifie la valeur dans la colonne spécifiée
                else:
                    ligne["total_sprint"]=int(valeur)
                break
    #modifie la valeur de total_marathon dans le csv
    elif mode_jeu=="marathon":
        for ligne in lignes:
            if ligne["Pseudo"] == username:
                if ligne["total_marathon"] is not None and ligne["total_marathon"] != '':
                    ligne["total_marathon"] = int(ligne["total_marathon"]) + int(valeur) #Modifie la valeur dans la colonne spécifiée
                else:
                    ligne["total_marathon"]=int(valeur)
    fichier_csv.close()
    #Réécrit les lignes modifiées dans le fichier CSV
    with open("./compte.csv", mode="w", newline='') as fichier_csv:
        noms_colonnes = ["Pseudo", "Mdp","total_sprint","total_marathon","ach1","ach2", "ach3","ach4","ach5","ach6","ach7","ach8","ach9","ach10","ach11","ach12","ach13","ach14","ach15","ach16","nb_partie_sprint","nb_partie_marathon","9","8","7","6","5","4","3","2","1","Score_sprint","Score_mara","nb_mot_marathon","dernier_temps"]               
        ecrivain = csv.DictWriter(fichier_csv, fieldnames=noms_colonnes)
        ecrivain.writeheader()
        ecrivain.writerows(lignes)
    fichier_csv.close()

def mettre_à_jour_donnees_vide():
    #Liste des donnees à vérifier et remplacer
    donnees_a_verifier = ["nb_partie_sprint", "Score_sprint", "total_sprint",
                       "nb_partie_marathon", "Score_mara", "total_marathon",
                       "nb_mot_marathon","dernier_temps"]
    
    for chemin in chemins:
        if os.path.exists(chemin):
            with open(chemin, mode="r", newline='') as fichier_csv: #Ouvrir le fichier CSV en mode lecture
                lecteur_csv = csv.DictReader(fichier_csv)
                donnees = list(lecteur_csv)
    for ligne in donnees: 
        if ligne["Pseudo"] == username:#Rechercher la ligne correspondant au pseudonyme spécifié
            #Parcourir les donnees à vérifier et remplacer les valeurs vides par 0
            for donnee in donnees_a_verifier:
                if ligne[donnee] == '' or ligne[donnee] is None:
                    ligne[donnee] = 0
    #Réécrire les données dans le fichier CSV
    for chemin in chemins:
        if os.path.exists(chemin):
            with open(chemin, mode="w", newline='') as fichier_csv:
                noms_colonnes = ["Pseudo", "Mdp","total_sprint","total_marathon","ach1","ach2", "ach3","ach4","ach5","ach6","ach7","ach8","ach9","ach10","ach11","ach12","ach13","ach14","ach15","ach16","nb_partie_sprint","nb_partie_marathon","9","8","7","6","5","4","3","2","1","Score_sprint","Score_mara","nb_mot_marathon","dernier_temps"]               
                ecrivain = csv.DictWriter(fichier_csv, fieldnames=noms_colonnes)
                ecrivain.writeheader()
                ecrivain.writerows(donnees)

def compte():
    accueil.withdraw()
    Stat.deiconify()
    Stat.title("Compte")
    Stat.geometry("500x500+400+100")
    Stat.config(bg=couleur)
    def creer_graphique(): #Fonction pour créer le graphique camembert dans la fenêtre tkinter
        #Charger les données CSV
        for chemin in chemins:
            if os.path.exists(chemin):
                df = pd.read_csv(chemin)
                break
        for chemin in chemins:
            if os.path.exists(chemin):
                with open(chemin, mode="r", newline='') as fichier_csv:
                    lecteur_csv = csv.DictReader(fichier_csv)
                    donnees = list(lecteur_csv)
        for ligne in donnees: 
            if ligne["Pseudo"] == username: #Trouve la ligne correspondant au pseudonyme spécifié
                #Label Statistique
                label_temps.place(x=30,y=280)
                w_nb_partie_sprint=Label(Stat,text="Vous avez joué "+ ligne["nb_partie_sprint"]+" parties en mode sprint",bg=couleur,font=("Arial",8))
                w_nb_partie_sprint.place(x=10,y=320)
                w_score_max_sprint=Label(Stat,text="Votre score maximum en mode sprint\n est de "+ligne["Score_sprint"]+"pts",bg=couleur,font=("Arial",8))
                w_score_max_sprint.place(x=30,y=360)
                w_score_total_sprint=Label(Stat,text="Votre score cumulé en mode sprint\n est de "+ligne["total_sprint"]+"pts",bg=couleur,font=("Arial",8))
                w_score_total_sprint.place(x=30,y=400)
                if int(ligne["nb_partie_sprint"]) != 0:
                    w_score_moy_sprint=Label(Stat,text="Votre score moyen en mode sprint\n est de "+str(round(int(ligne["total_sprint"])/int(ligne["nb_partie_sprint"]),2))+"pts",bg=couleur,font=("Arial",8))
                    w_score_moy_sprint.place(x=30,y=450)
                w_nb_partie_marathon=Label(Stat,text="Vous avez joué "+ ligne["nb_partie_marathon"]+" parties en mode marathon",bg=couleur,font=("Arial",8))
                w_nb_partie_marathon.place(x=262,y=280)
                w_score_max_marathon=Label(Stat,text="Votre score maximum en mode marathon\n est de "+ligne["Score_mara"]+"pts",bg=couleur,font=("Arial",8))
                w_score_max_marathon.place(x=280,y=360)
                w_score_total_marathon=Label(Stat,text="Votre score cumulé en mode marathon\n est de "+ligne["total_marathon"]+"pts",bg=couleur,font=("Arial",8))
                w_score_total_marathon.place(x=280,y=400)
                if int(ligne["nb_partie_marathon"]) !=0:
                    w_score_moy_marathon=Label(Stat,text="Votre score moyen en mode marathon\n est de "+str(round(int(ligne["total_marathon"])/int(ligne["nb_partie_marathon"]),2))+"pts",bg=couleur,font=("Arial",8))
                    w_score_moy_marathon.place(x=280,y=450)
                w_max_mot_marathon=Label(Stat,text="Votre nombre de mots trouvés en une partie\n du mode marathon est de "+ligne["nb_mot_marathon"]+" mots",bg=couleur,font=("Arial",8))
                w_max_mot_marathon.place(x=280,y=320)
                #Création du canvas en barre pour séparer les stats
                séparation = Canvas(Stat, width=2, height=280, bg="black",highlightbackground=couleur)
                séparation.place(x=248,y=220)
                colonnes = [str(i) for i in range(1, 10)] #Extraire les colonnes spécifiques pour ce pseudonyme
                data = df.loc[df['Pseudo'] == username, colonnes]
                data.fillna(0, inplace=True) #Remplacer les valeurs manquantes par zéro 
                data_non_zero = data.loc[:, (data != 0).any(axis=0)] #Filtrer les colonnes pour ne conserver que celles avec des valeurs différentes de zéro
                fig, ax = plt.subplots() #Créer le graphique camembert
                wedges, texts, autotexts =ax.pie(data_non_zero.iloc[0], labels=[str(i) for i in data_non_zero.columns], autopct='%1.1f%%', startangle=140)
                ax.set_title('Nombre de lettres des mots trouvés',fontsize=9)
                fig.patch.set_facecolor(couleur)
                #modifier taille du texte
                for text in texts:
                    text.set_size(8)
                for autotext in autotexts:
                    autotext.set_size(8)

                #Intégrer le graphique dans la fenêtre tkinter
                canvas = FigureCanvasTkAgg(fig, master=Stat)
                canvas.get_tk_widget().config(width=270, height=250, bg=couleur)
                canvas.get_tk_widget().place(x=120, y=20)
                canvas.draw()
                break  

    #Appel la fonction
    creer_graphique()
    #création des bouton quitter et retouer
    retour = customtkinter.CTkButton(Stat, text="Retour à l'accueil",fg_color="#34C0E2",hover_color='#CAC8C8',text_color="black",width=70,height=20,border_width=1,border_color='black', command=retour_accueil)
    retour.place(x= 10, y=5)
    quitter = customtkinter.CTkButton(Stat,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
    quitter.place(x=440,y=5)

def creation_compte(): #fonction pour se connecter
    compte = Toplevel(connexion) #Création de la fenêtre compte
    #parametre de la fentre compte
    compte.title("Connectez-vous à votre compte")
    compte.geometry("200x200+500+150")
    compte.configure(bg=couleur)
    #créatio  du bouton quitter
    quitter=Button(best, text="quitter", command=quits,bg="Red")
    quitter.place(x=450,y=0)
    #fonction pour verifier l'éxistance du Pseudo
    def username_existe_dans_colonne(username, nom_colonne):
        with open("./donnees/compte.csv", mode="r", newline='') as fichier_csv:
            lecteur_csv = csv.DictReader(fichier_csv)
            for ligne in lecteur_csv:
                if ligne[nom_colonne] == username:
                    return True
        fichier_csv.close()
        return False
    #fonction pour vérifier l'éxistance entre du mdp
    def password_existe_dans_colonne(password, nom_colonne):
        with open("./donnees/compte.csv", mode="r", newline='') as fichier_csv:
            lecteur_csv = csv.DictReader(fichier_csv)
            for ligne in lecteur_csv:
                if ligne[nom_colonne] == password:
                    return True
        fichier_csv.close()
        return False
    #fonction de connection
    def login():
        global username
        username = entry_username.get()
        password = entry_password.get()

        if username_existe_dans_colonne(username, "Pseudo") == True and password_existe_dans_colonne(password, "Mdp") == True:
            compte.withdraw()
            page_accueil()
            commencer_timer()
            actualiser_temps()
        else:
            compte.withdraw()
            if username_existe_dans_colonne(username, "Pseudo") == True and password_existe_dans_colonne(password, "Mdp") == False:
                messagebox.showerror("Erreur d'authentification", "Le mot de passe est incorrect")#erreur messagebox car mdp incorrect
            elif username_existe_dans_colonne(username, "Pseudo") == False and password_existe_dans_colonne(password, "Mdp") == True:
                messagebox.showerror("Erreur d'authentification", "Ce compte n'existe pas")#erreur messagebox car Pseudo incorrect
            elif username_existe_dans_colonne(username, "Pseudo") == False and password_existe_dans_colonne(password, "Mdp") == False:
                messagebox.showerror("Erreur d'authentification", "Ce compte n'existe pas") #erreur messagebox car mdp et Pseudo incorrect

    #création du label d'entré du Pseudo
    label_username = Label(compte, text="Pseudonyme:",bg=couleur)
    label_username.pack()
    label_username.place(x=20, y=15)
    entry_username = Entry(compte)
    entry_username.pack()
    entry_username.place(x=20, y=40)

    #création du label mdp
    label_password = Label(compte, text="Mot De Passe:",bg=couleur)
    label_password.pack()
    label_password.place(x=20, y=70)
    entry_password = Entry(compte, show="*")
    entry_password.pack()
    entry_password.place(x=20, y=100)

    #Bouton connexion
    login_button = Button(compte, text="Se connecter", command=login)
    login_button.pack()
    login_button.place(x=60, y=140)

#fonction pour se creer un compte
def inscription():
    #Création de la fenêtre tkinter et configuration
    enregistrer = Toplevel(connexion)
    enregistrer.title("Enregistrement d'informations")
    enregistrer.geometry("200x200+500+150")
    enregistrer.configure(bg=couleur)
    #Vérification de l'éxistence du Pseudo et mdp
    def present(nom_colonne,mot):
        with open("donnees/compte.csv", mode="r", newline='') as fichier_csv:
            lecteur_csv = csv.DictReader(fichier_csv)
            for ligne in lecteur_csv:
                if ligne[nom_colonne] == mot:
                    return False
        fichier_csv.close()
        return True
    #fonction pour enregister les nouveaux compte dans le csv
    def enregistrer_infos():
        nom = entry_nom.get()
        password = entry_password.get()
        #Ouverture du fichier CSV en mode écriture
        with open("donnees/compte.csv", mode="a", newline='') as fichier_csv:
            writer = csv.writer(fichier_csv)
            if present("Pseudo",nom) and present("Mdp",nom) ==True:
                writer.writerow([nom, password])
                enregistrer.withdraw()
            else:
                label_erreur=Label(enregistrer, text="Ce compte existe déjà",bg="RED")
                label_erreur.place(x=40, y=0)
            fichier_csv.close()

    # Création des étiquettes et des champs de saisie
    nom_label = Label(enregistrer, text="Nom :", bg=couleur)
    nom_label.grid(row=0, column=0)
    nom_label.place(x=20, y=15)
    mdp_label = Label(enregistrer, text="Mot de Passe :", bg=couleur)
    mdp_label.grid(row=1, column=0)
    mdp_label.place(x=20, y=70)

    entry_nom = Entry(enregistrer)
    entry_nom.grid(row=0, column=1)
    entry_nom.place(x=20, y=40)
    entry_password = Entry(enregistrer)
    entry_password.grid(row=1, column=1)
    entry_password.place(x=20, y=100)

    # Création du bouton pour enregistrer les informations
    bouton_enregistrer = Button(enregistrer, text="Enregistrer", command=enregistrer_infos)
    bouton_enregistrer.grid(row=2, columnspan=2)
    bouton_enregistrer.place(x=60, y= 140)

label_text=Label(connexion,text="Veuillez vous connecter pour accéder au jeu",font=('Aldus', 14), bg=couleur)
label_text.place(x=60, y=100)
#creation des boutons login et register
login = customtkinter.CTkButton(connexion, text="CONNEXION", width=150, height=90,fg_color="#C2CABF",text_color="black",corner_radius=14,command=creation_compte)
login.place(x=50,y=200)
register = customtkinter.CTkButton(connexion, text="INSCRIVEZ-VOUS", width=150, height=90,fg_color="#C2CABF",text_color="black",corner_radius=14,command=inscription)
register.place(x=300,y=200)
quitter = customtkinter.CTkButton(connexion,text="Quitter", width=50, height=20,fg_color="red",text_color="black",hover_color="#A12929",corner_radius=12, command=quits)
quitter.place(x=430, y=11)

#calcule le temps de jeu

def convertir_temps(secondes):
    heures = secondes // 3600
    secondes %= 3600
    minutes = secondes // 60
    secondes %= 60
    return "{:02}:{:02}:{:02}".format(int(heures), int(minutes), int(secondes))

def  charger_dernier_temps():
    global donnees
    for chemin in chemins:
        if os.path.exists(chemin):
            with open(chemin, mode="r", newline='') as fichier_csv:
                lecteur_csv = csv.DictReader(fichier_csv)
                donnees = list(lecteur_csv)
    for ligne in donnees:
        if ligne["Pseudo"]==username:
            if ligne["dernier_temps"] is not None or ligne["dernier_temps"]!='':
                try:
                    return float(ligne["dernier_temps"])
                except:
                    return 0
def commencer_timer():
    global temps_debut
    temps_debut = time.time() - charger_dernier_temps()

label_temps = Label(Stat, text="Temps de jeu: 00:00:00",bg=couleur)

def actualiser_temps():
    if temps_debut:
        temps_actuel = int(time.time() - temps_debut)
        label_temps.config(text="Temps de jeu: " + convertir_temps(temps_actuel),bg=couleur)
    connexion.after(1000, actualiser_temps)

mainloop()
