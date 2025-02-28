#                   PARTIE A

#1

def init(n):
    liste=[]                    #liste représente l'ensemble des disques empilé (dans l'ordre décroissant) sur la tour la plus à gauche 
    while n>=1:                 #empilement des n disques 
        liste+=[n]
        n-=1
    res=[liste,[],[]]           #les tours du milieu et de droite sont forcément vide au début du jeu
    return res


#2

def nbDisques(plateau,numtour):
    res=len(plateau[numtour])   #calcul la longeur à un tour donné et donc le nombre de disque disposé sur celle ci
    return res

#3

def disqueSup(plateau,numtour):
    config=plateau[numtour]     #prend la configuration de disque(s) à la tour demandé 
    if config!=[]:
        res=config[-1]          #si il y a un ou plusieurs disque(s), res prend la valeur du disque le plus en haut de la tour
    else :
        res=-1                  #si la tour est vide le programme renvoie -1
    return res

#4

def posDisque(plateau,numdisque):
    trouvé=False                        #initialisation de l'indice à 0 pour la première tour et d'un boléen afin de parcourir le jeu jusqu'à ce que la position du disque demandé soit touvé et rapporté
    i=0
    while not trouvé :                  #le disque est forcément sur la tour 0,1 ou 2 donc pas besoin de mettre une condition supplémentaire sur la boucle while sur i
        if numdisque in plateau[i]:     #lorsque la tour sur laquelle est le disque est trouvée, on garde le numéro de cette tour et on arrête la boucle (un disque ne peut pas être sur 2 tour en même temps) 
            trouvé=True
            res=i
        i+=1
    return res

#5

def verifDepl(plateau,nt1,nt2):
    res=True                                                                            #initialisation de la réponse sous forme de boléen
    if disqueSup(plateau,nt1)==-1 or disqueSup(plateau,nt1)>=disqueSup(plateau,nt2):    #les conditions pour que le coup demandé ne puisse pas être joué sont : - il n'y a pas de disque la tour nt1 demandée
        res=False                                                                       #                                                                       - il y a un disque mais celui-ci est plus grand que le plus haut disque de la tour nt2 demandée
    if disqueSup(plateau,nt2)==-1:                                                      #si la tour nt2 est vide le coup peut être joué à tous les coups
        res=True                                                                        #or -1 < 1 donc ce cas doit être traité (-1 étant la valeur renvoyé pour une tour vide et 1 le plus petit nombre de disque possible)
    return res

#6

def verifVictoire(plateau,n):
    liste=[]                        #liste représente l'ensemble des disques empilé (dans l'ordre décroissant) sur la tour la plus à droite
    res=False                       #initialisation réponse
    while n>=1:                     #empilement des n disques
        liste+=[n]
        n-=1
    victoire=[[],[],liste]          #liste qui doit être obtenue en cas de victoire, les tours du milieu et de gauche sont forcément vide en cas de victoire
    if plateau==victoire:           #condition de victoire vérifiée
        res=True
    return res


#                   PARTIE B

import turtle



def remplissage(n):                                                     #création d'un dictionnaire qui au numéro du disque associe sa couleur
    liste = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    couleurs={}
    for i in range(n):
        if i>=len(liste):
            k=i%len(liste)
            couleurs[i+1]=liste[k]
        else:
            couleurs[i+1]=liste[i]
    return couleurs

#1

def dessinePlateau(n):

    turtle.hideturtle()

    h_disque=400/(n+3)

    if n<=5:
        h_plateau=1.5*h_disque
    elif n<=10:
        h_plateau=2*h_disque
    else:
        h_plateau=80

    L_plateau=600
    h_tour=400-h_plateau
    L_tour=10
    n_max=(L_plateau-2*15)//3                       #écart de 15 de chaque côtés


#trace plateau

    turtle.up()
    turtle.goto(-300,-200)                     #point de départ du plateau
    turtle.down()

    turtle.fillcolor('brown')
    turtle.begin_fill()

    for i in range (2):
        turtle.forward(L_plateau)
        turtle.right(90)
        turtle.forward(h_plateau)
        turtle.right(90)
    
    


#trace les tours

    turtle.forward(15+1/2*n_max-1/2*L_tour)              #on avance de 15 de chaque côté, plus le moitié de la longueur du plus grand disque moins la moitié de l'épaisseur de la tour

    for i in range (3):

#trace 1ère tour 

        turtle.left(90)
        turtle.forward(h_tour)
        turtle.right(90)
        turtle.forward(L_tour)
        turtle.right(90)
        turtle.forward(h_tour)

        turtle.up()
        
        turtle.left(90)
        turtle.forward(n_max-L_tour)                    #laisse la longeur du disque le plus grand pour qu'ils ne se touchent jamais

        turtle.down()

    turtle.end_fill()

    turtle.up()
    turtle.goto(-300,-200)


#2

def dessineDisque(nd,plateau,n):
    couleur=remplissage(nd)[nd]
    tour=posDisque(plateau,nd)
    
    if n<=5:
        h_plateau=1.5*400/(n+3)
    elif n<=10:
        h_plateau=2*400/(n+3)
    else:
        h_plateau=80

    n_min=20                                        #longueur du plus petit disque
    L_plateau=600
    h_tour=400-h_plateau
    h_disque=h_tour/(n+1)
    L_tour=10
    n_max=(L_plateau-2*15)//3                       #écart de 15 de chaque côtés
    L_disque=n_max
    
    if n<=3:
        ecart=40
    elif n<=5:                                        #pour que le jeu soit jolie avec peu de disques
        ecart=25                                    #ecart de longueur entre deux disques successifs
    elif n<=10:
        ecart=18
    else:                                           #pour que le jeu soit possible avec bcp de disques
        ecart=(n_max-n_min)/n

    for i in range(n-nd+1):
        L_disque-=ecart                               #enleve 15 pour pour chaque disque qui sépare le disque voulu avec le plus grand
    if L_disque%2==1:
        L_disque+=1                                 #pour ne pas avoir à faire à des dimensions non paires qui lorsqu'on va avancer de la moitié de leur longueur va donner un entier et donv un trait non droit

#calcul étage disque

    etage=0
    liste_tour=plateau[tour]                        #liste_tour représente l'ensemble des disques à la tour où l'on veut dessiner le disque      
    for i in range (len(liste_tour)):
        if liste_tour[i]>nd:
            etage+=1

    turtle.up()
    turtle.goto(-300,-200)                     #point de départ du plateau

#aller à la bonne tour

    turtle.forward(15+(1/2+tour)*n_max)             #on avance de 15 (marge de départ)+ la moitié de la longueur du plus grand disque pour arriver au milieur de la première tour + n fois pour arriver à la bonne tour

#aller au bon étage

    turtle.left(90)
    turtle.forward(etage*h_disque)
    turtle.right(90)

#efface tour au niveau du disque

    turtle.color('white')
    turtle.forward(L_tour/2)

    turtle.left(90)
    turtle.forward(1)
    turtle.down()
    turtle.forward(h_disque-1)
    turtle.left(90)
    turtle.up()
    turtle.forward(L_tour)
    turtle.down()
    turtle.left(90)
    turtle.forward(h_disque)
    turtle.left(90)
    turtle.up()
    turtle.forward(L_tour)
    turtle.color('black')
    turtle.backward(L_tour/2)

#dessine disque

    turtle.fillcolor(couleur)                       #prendre la couleur adapté au disque
    turtle.begin_fill()

    turtle.up()
    turtle.backward(1/2*L_disque)
    turtle.down()
    for i in range(2):
        turtle.forward(L_disque)
        turtle.left(90)
        turtle.forward(h_disque)
        turtle.left(90)
    turtle.end_fill()

#3

def effaceDisque(nd,plateau,n):

    tour=posDisque(plateau,nd)
    

    if n<=5:
        h_plateau=1.5*400/(n+3)
    elif n<=10:
        h_plateau=2*400/(n+3)
    else:
        h_plateau=80

    n_min=20                                        #longueur du plus petit disque
    L_plateau=600
    h_tour=400-h_plateau
    h_disque=h_tour/(n+1)
    L_tour=10
    n_max=(L_plateau-2*15)//3                       #écart de 15 de chaque côtés
    L_disque=n_max

    if n<=3:
        ecart=35
    elif n<=5:
        ecart=25
    elif n<=10:
        ecart=18
    else:
        ecart=(n_max-n_min)/n

    for i in range(n-nd+1):
        L_disque-=ecart                               #enleve 15 pour pour chaque disque qui sépare le disque voulu avec le plus grand
    if L_disque%2==1:
        L_disque+=1                                 #pour ne pas avoir à faire à des dimensions non paires qui lorsqu'on va avancer de la moitié de leur longueur va donner un entier et donv un trait non droit

#calcul étage disque

    etage=0
    liste_tour=plateau[tour]                        #liste_tour représente l'ensemble des disques à la tour où l'on veut dessiner le disque      
    for i in range (len(liste_tour)):
        if liste_tour[i]>nd:
            etage+=1

    turtle.up()
    turtle.goto(-300,-200)                     #point de départ du plateau

#aller à la bonne tour

    turtle.forward(15+(1/2+tour)*n_max)             #on avance de 15 (marge de départ)+ la moitié de la longueur du plus grand disque pour arriver au milieur de la première tour + n fois pour arriver à la bonne tour

#aller au bon étage

    turtle.left(90)
    turtle.forward(etage*h_disque)
    turtle.right(90)

#efface disque (sans effacer le côté bas du disque car cela efface soit le disque en dessous soit le plateau)

    turtle.fillcolor('white')
    turtle.begin_fill()

    turtle.color('white')
    turtle.up()
    turtle.backward(L_disque/2)
    turtle.forward(L_disque)
    turtle.left(90)
    turtle.forward(1)                   #pour éviter d'effacer un pixel du haut du disque ou du plateau situé en dessous
    turtle.down()
    turtle.forward(h_disque-1)
    turtle.left(90)
    turtle.forward(L_disque)
    turtle.left(90)
    turtle.forward(h_disque)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.color('black')
    turtle.forward(1/2*L_disque)

#retrace tour au niveau du disque

    turtle.fillcolor('brown')
    turtle.begin_fill()

    turtle.forward(L_tour/2)

    turtle.down()
    turtle.left(90)
    turtle.forward(h_disque+1)              #pour éviter d'effacer un pixel du haut du disque ou du plateau situé en dessous
    turtle.left(90)
    turtle.up()
    turtle.forward(L_tour)
    turtle.down()
    turtle.left(90)
    turtle.forward(h_disque+1)
    turtle.left(90)
    turtle.forward(L_tour)


    turtle.end_fill()
    turtle.up()
    turtle.forward(L_tour/2)



#4

def dessineConfig(plateau,n):
    for i in range (1,n+1): 
        dessineDisque(i,plateau,n)

#5

def effaceTout(plateau,n):
    for i in range (1,n+1):
        effaceDisque(i,plateau,n)


#               PARTIE D

#1



def dernierCoup(coups):
    clef=len(coups)-1                    # -1 car le premier terme du dictionnaire est le coup 0 a qui est associé la position initiale
    precedent=coups[clef-1]
    actuel=coups[clef]
    for i in range (3):
        if actuel[i]!=precedent[i] and len(precedent[i])<len(actuel[i]):    #pour trouver le numéro du disque qui a été deplacé il faut trouver sur quelle tour les combinaisons de disque ne sont pas les mêmes
            numdisque=actuel[i][-1]                                         #et sur quelle tour il y a plus de disque (car une tour peut avoir une combinaisons différente mais ne pas comporter le disque qui a été déplacé)
    return numdisque


#2

def annulerDernierCoup(coups):
    clef=len(coups)-1
    del coups[clef]

#                   PARTIE F

#1 et #2


def solution(n,tour0=0, tour2=2, tour1=1):

    deplacement=[]

    def solution_deplacement(n,tour0=0, tour2=2, tour1=1):          #ajoute à deplacement toutes les listes des couples des deux tours à jouer(deplacer le disque de la tour a à la tour b)
        if n == 1:                                                  #par exemple pour n=3 deplacement=[[0, 1], [0, 2], [1, 2]]
                                                                    #met cette fonction dans l'autre car permet de réunitialiser deplacement et ainsi de pouvoir demander plusieurs solutions dans l'algorythme
            return deplacement.append([tour0, tour2]) 
        solution_deplacement(n-1, tour0, tour1, tour2)

        deplacement.append([tour0, tour2])
        solution_deplacement(n-1, tour1, tour2, tour0)

    solution_deplacement(n)                                     #utilise deplacement pour en faire un dictionnaire qui au numeor de coup associe les positions des disques sur le jeu
    
    plateau=init(n)                                             #initialisation situation initiale
    solve={0:copy.deepcopy(plateau)}                        

    for i in range (0,2**n-1):                                  #on gagne toujours en 2**n-1 coups
        dep=deplacement[i][0]                                   #prend la valeur de la tour de départ à jouer

        arr=deplacement[i][1]                                   #prend la valeur de la tour d'arrivée à jouer

        disque=disqueSup(plateau,dep)                           #prend le numéro du disque qui va être déplacé

        plateau[dep].remove(disque)                             #change plateau pour déplacer le disque joué 
        plateau[arr].append(disque)
        solve[i+1]=copy.deepcopy(plateau)                       #et l'enregistrer dans le dictionnaire


    return deplacement,solve                                                #retourne les couples de déplacements et toutes les combinaisons dans l'ordre à jouer 

#                   PARTIE C


#1

def lireCoords(plateau,cpt):
    
    coup="Coup",cpt                                                                                #variable qui va servir à afficher le numéro du coups dans le jeu
    dep=turtle.textinput(coup,"Tour de départ? ")                                                               #recherche tour de départ
    #dep est un str pour que quoi que le joueur saisisse le programme ne plante pas 
    while dep not in ['0','1','2'] or disqueSup(plateau,int(dep))==-1 or (not verifDepl(plateau,int(dep),0) and not verifDepl(plateau,int(dep),1) and not verifDepl(plateau,int(dep),2)):    #la tour n'est pas valide lorsque : - elle n'est pans comprise entre 0 et 2 inclus - soit il n'y a pas de disque sur la tour selectionnée - soit le disque selectionné ne peut pas être déplacé (lorsqu'il est plus grand que le sommet de chacunes des autres tours)
        if dep=='-1':                                                                             #ajout de la possibilité du joueur à abandonner la partie lorsqu'il donne -1 à la valeur de la tour de départ
            rep=turtle.textinput(coup,"Tu souhaites abandonner (o/n)? ")
            while rep not in ["o","n"]:
                rep=turtle.textinput(coup,"Tu souhaites abandonner (o/n)? ")
            if rep == "o":
                abandon=True
                return abandon,33                                                               #return un des informations singulières pour pouvoir être traitées après
            else:
                dep=turtle.textinput(coup,"Tour de départ? ")

            
        elif dep=='-2':                                                                             #ajout de la possibilité de revenir au coup précédent
            rep=turtle.textinput(coup,"Tu souhaites revenir au coup prédédent (o/n)? ")
            while rep not in ["o","n"]:
                rep=turtle.textinput(coup,"Tu souhaites revenir au coup prédédent (o/n)? ")
            if rep=="o":
                annuler=True                                                                    #return un des informations singulières pour pouvoir être traitées après
                return 33,23
            else:
                dep=turtle.textinput(coup,"Tour de départ? ")


        elif dep not in ['0','1','2']:                                                          #si la tour de départ ne correspond pas à une tour on redemande de saisir un numéro de tour avec un message qui indique dans chaque cas pourquoi la saisie ne correspond pas à un choix possible
            dep=turtle.textinput(coup,"Invalide, tour innexistante. Tour de départ? ")          
        elif disqueSup(plateau,int(dep))==-1:
            dep=turtle.textinput(coup,"Invalide, la tour ne contient pas de disque. Tour de départ? ")
        else :
            dep=turtle.textinput(coup,"Invalide, le disque au sommet de la tour ne peux pas être déplacé. Tour de départ? ")         #une réponse différente et précise sera affichée pour chaque type de problème
                                                                                                                                         #ainsi qu'une nouvelle valeur de la tour de départ

    arr=turtle.textinput(coup,"Tour d'arrivée? ")                                                               #recherche tour d'arrivée
    while arr==dep or arr not in ['0','1','2'] or not verifDepl(plateau,int(dep),int(arr)):      #la tour d'arrivéé ne fonctionne pas lorsque : - elle est la même que la tour de départ (dans ce cas, rien ne se passe) - elle n'est pas comprise entre 0 et 2 inclus - le disque supérieur de la tour d'arrivée est plus petit que celle de la tour de départ
        if arr==dep:
            arr=turtle.textinput(coup,"Invalide, tour identique. Tour d'arrivée? ")
        elif arr not in ['0','1','2']:
            arr=turtle.textinput(coup,"Invalide, tour innexistante. Tour d'arrivée? ")
        else:                                                                                   #une réponse différente et précise sera affichée pour chaque type de problème
            arr=turtle.textinput(coup,"Invalide, disque plus petit. Tour d'arrivée? ")                                               #ainsi qu'une nouvelle valeur de la tour d'arrivée

    return int(dep),int(arr)                                                                    #retourne les reponses saisies sous forme d'entiers pour pouvoir être traités par la suite


#2

def jouerUnCoup(plateau,n,cpt):
    dep,arr=lireCoords(plateau,cpt)
    if type(dep)==bool:                                     #si dep est un bool c'est que le joueur veut abandonner
        return dep,arr
    elif dep!=33:                                           #si dep=33 le joueur veut revenir en arrière
        effaceDisque(plateau[dep][-1],plateau,n)
        plateau[arr].append(plateau[dep][-1])               #rajoute le disque déplacé à la bonne tour
        plateau[dep].remove(plateau[dep][-1])               #enlève le disque déplacé de la tour de départ
        dessineDisque(plateau[arr][-1],plateau,n)
    return dep,arr

#3

import copy

def boucleJeu(plateau,n):
    nb_essais=2**(n+1)                                                                  #en sachant due de manière optimale on gagne avec 2**(n)-1 coups
    cpt=1
    coups={0:init(n)}
    dep,arr=jouerUnCoup(plateau,n,cpt)
    while not verifVictoire(plateau,n) and cpt<nb_essais and type(dep)!=bool :          #si dep est un bool c'est parce que le joueur à abandonné la partie
        if dep==33 and cpt>1:                                                           #si le joueur a voulu annuler son coup et qu'il peut l'être
            nd=dernierCoup(coups)
            effaceDisque(nd,coups[len(coups)-1],n)
            dessineDisque(nd,coups[len(coups)-2],n)
            annulerDernierCoup(coups)
            cpt-=1
            turtle.textinput("Coup annulé","Retour au coup précédent")
            plateau=coups[len(coups)-1]
        elif dep!=33:                                                                          #si le coup n'a pas été un retour en arrière on joue normalement
            coups[cpt]=copy.deepcopy(plateau)                                                  #copy.deepcopy car sinon change toutes les valeurs du dictionnaire
            cpt+=1
        else :                                                                                 #si le coup ne peut pas être annulé
            turtle.textinput("Impossible","Tu es déjà à la position initiale")
        dep,arr=jouerUnCoup(plateau,n,cpt)
    

    #pour chaque situation de fin de partie on affiche un message unique
    if verifVictoire(plateau,n)==True :                                                 #si le joueur gagne
        txt="Gagné après "+str(cpt)+" coups !"
        turtle.textinput("Victoire",txt)
        return True,cpt,plateau
    elif cpt==nb_essais:                                                                #si le joueur perds car il a fait trop d'essais
        txt="Les "+str(nb_essais)+" essais sont écoulés!"
        turtle.textinput("Défaite",txt)
    elif dep==True:                                                                     #si le joueur abandonne
        if arr==33:
            cpt-=1
            txt="Abandon de la partie après "+str(cpt)+" coups."
            turtle.textinput("Défaite",txt)
            
            soluce=turtle.textinput("Défaite","Voulez vous voir la solution ? (o/n)")
            while soluce not in ["o","n"]:
                soluce=turtle.textinput("Défaite","Voulez vous voir la solution ? (o/n)")
            if soluce=="o":
                deplacement,dico_solution=solution(n)
                effaceTout(plateau,n)
                dessineConfig(dico_solution[0],n)
                for i in range(0,2**n-1):
                    
                    effaceDisque(disqueSup(dico_solution[i],deplacement[i][0]),dico_solution[i],n)
                    dessineDisque(disqueSup(dico_solution[i],deplacement[i][0]),dico_solution[i+1],n)
                    plateau=copy.deepcopy(dico_solution[i+1])

    return False,0,plateau

            
#                   PARTIE E 

import time

#1

def sauvScore (liste_scores,nb_disque,coups):
    nom=turtle.textinput("Enregistrement score","Quel est ton nom ? ")
    score={"nom":nom}
    for i in range (len(liste_scores)):
        d=liste_scores[i]
        if d["nom"]==nom:                           #si le nom est déjà enregistré on ajoute le score au dictionnaire de scores du nom
            if nb_disque in d:                      #si le nb_disque de la partie est deja dans le dictionnaire de score du joueur,on ajoute la score de cette partie
                d[nb_disque].append(coups)
            else :
                d[nb_disque]=[coups]                #si c'est la première partie avec ce nombre de disque, on crée un emplacement dans le dictionnaire qui au nombre de disque associe le score
            liste_scores.pop(i)
            liste_scores.append(d)
            return liste_scores

    score[nb_disque]=[coups]                        #si le nom du joueur n'est pas enregistré, on créé un dictionnaire avec son nom, le nb de disques et son score de la partie
    liste_scores.append(score)                      #liste de la forme [{"nom":Nom1,disque1:[coups1,coups2],disques2:[coups3]},{"nom":Nom2,disque3:[coups4],disques2:[coups5]}]
    return liste_scores,nom

#2

def calcul_temps(debut,fin):
    temps=[]                                                                     #temps represente le temps de jeu (la différence entre fin et debut) sous forme [année,mois,jour,heure,minute,seconde]
    for i in range (len(fin)):
        if fin[i]>debut[i] and i!=5:
            fin[i]-=1
            if i==0:                                                            #si c'est une année, on la convertie en 12 mois
                adapte=12
            elif i==1:                                                          #si c'est un mois, on le converti en jours 
                if debut[i] in [1,3,5,7,8,10,12]:                               #soit 31 jours 
                    adapte=31
                elif debut[i]!=2:                                               #soit 30 jours 
                    adapte=30
                else:
                    if (debut[0]%4==0 and debut[0]%100!=0) or debut[0]%400==0:  #soit 28 ou 29 jours si le mois est février et suivant si l'année est bissextile ou non
                        adapte=29
                    else:
                        adapte=28
            elif i==2:                                                          #si c'est un jour, on le convertie en 24h
                adapte=24
            elif i==3 or i==4:                                                  #si c'est une heure, on la convertie en 60mins et si c'est une minute en 60 secs
                adapte=60
            
            fin[i+1]+=adapte                                                    #on ajoute la conversion à l'unité de temps au rang suivant
        temps.append(fin[i]-debut[i])
    return temps

#4

def afficheScores(liste_scores,nb_disque):
    scores=liste_scores
    continu=False
    execo=False
    for i in scores:                      #si aucune partie n'a été gagnée avec le nombre de disque demandé on redemande 
        if nb_disque in i:
            continu=True
        else:
            return 0
    print("Podium pour les parties à",nb_disque,"disques en fonction des coups")
    print("")
    if continu:
        meilleur=None
        for i in range (1,4):                     #montre les 3 scores sur le podium
            meilleur_precedent=meilleur
            nom=None
            meilleur=10*100
            for d in scores:              #parcours les joueurs
                m=meilleur
                if d[nb_disque]!=None:
                    for c in d[nb_disque]:          #parcours les scores avec le nombre de disques voulus
                        if m>c and meilleur>c:
                            m=c
                            n=d["nom"]
                if meilleur>m:                      #si le score d'un autre joueur est meilleur que celui retenu, alors on l'enregistre en tant que meilleur joueur, sinon on change pas
                    meilleur=m
                    nom=n
            if nom!=None:
                if i==1:
                    print(i,"er :",nom,"avec",meilleur,"coups")
                elif i==2:
                    if meilleur!=meilleur_precedent:    #si le premier et le deuxième n'ont pas le même score
                        print(i,"eme :",nom,"avec",meilleur,"coups")
                    else:
                        print(i-1,"er :",nom,"avec",meilleur,"coups")
                        execo=True
                else:
                    if meilleur!=meilleur_precedent:
                        print(i,"eme :",nom,"avec",meilleur,"coups")
                    else:
                        if execo:
                            print(i-2,"er :",nom,"avec",meilleur,"coups")
                        else:
                            print(i-1,"eme : ",nom,"avec",meilleur,"coups")
            
                for k in scores:                                #enlève le score qui a été affiché 
                    if meilleur in k[nb_disque] and k["nom"]==nom:
                        k[nb_disque].remove(meilleur) 
    
    return 1

#5

def sauvChronos(liste_chronos,nb_disque,temps,nom):
    score={"nom":nom}
    for i in range (len(liste_chronos)):
        d=liste_chronos[i]
        if d["nom"]==nom:                           #si le nom est déjà enregistré on ajoute le score au dictionnaire de chrono du nom
            if nb_disque in d:                      #si le nb_disque de la partie est deja dans le dictionnaire de score du joueur,on ajoute la chrono de cette partie
                d[nb_disque].append(temps)
            else :
                d[nb_disque]=[temps]                #si c'est la première partie avec ce nombre de disque, on crée un emplacement dans le dictionnaire qui au nombre de disque associe au chrono
            liste_chronos.pop(i)
            liste_chronos.append(d)

    score[nb_disque]=[temps]                        #si le nom du joueur n'est pas enregistrer, on crée un dictionnaire avec son nom, le nb de disques et son chrono de la partie
    liste_chronos.append(score)
    return liste_chronos


def afficheChronos(liste_scores,nb_disque):
    scores=liste_scores
    continu=True
    execo=False
    print("")
    print("Podium pour les parties à",nb_disque,"disques en fonction du temps de jeu")
    print("")
    if continu:
        meilleur=None
        for i in range (1,4):                     #montre les 3 scores sur le podium
            meilleur_precedent=meilleur
            nom=None
            meilleur=[100,0,0,0,0,0]
            for d in scores:              #parcours les joueurs
                m=meilleur

                if d[nb_disque]!=None:
                    for c in d[nb_disque]:          #parcours les chronos avec le nombre de disques voulus

                        for x in c:

                            for e in range (6):

                                if m[e]>c[e] and meilleur[e]>c[e]:
                                    m=c
                                    n=d["nom"]

                if meilleur>m:                      #si le chrono d'un autre joueur est meilleur que celui retenu, alors on l'enregistre en tant que meilleur joueur, sinon on ne change pas
                    meilleur=m
                    nom=n
            
            enleve=True                             #pour reduire la liste [année,mois,jour,heure,minute,seconde] et enlever les premieres valeures qui sont égales à 0 et donc inutiles
            max=list(meilleur)
            while enleve :
                if max[0]==0:
                    max.pop(0)
                else:
                    enleve=False
            

            txt=""  
            for m in range(len(max)):
                variable=str(max[m])
                if m==len(max)-1:
                    txt+=variable+" secs "
                elif  m==len(max)-2:
                    txt+=variable+" min "
                elif  m==len(max)-3:
                    txt+=variable+" h "
                elif  m==len(max)-4:
                    txt+=variable+" j "
                elif  m==len(max)-5:
                    txt+=variable+" mois "
                elif  m==len(max)-6:
                    txt+=variable+" ans "

            if nom!=None:
                if i==1:
                    print(i,"er :",nom,"en",txt)
                elif i==2:
                    if meilleur!=meilleur_precedent:    #si le premier et le deuxième n'ont pas le même score
                        print(i,"eme :",nom,"en",txt)
                    else:
                        print(i-1,"er :",nom,"en",txt)
                        execo=True
                else:
                    if meilleur!=meilleur_precedent:
                        print(i,"eme :",nom,"en",txt)
                    else:
                        if execo:
                            print(i-2,"er :",nom,"en",txt)
                        else:
                            print(i-1,"eme : ",nom,"en",txt)

                for k in scores:                                #enlève le score qui a été affiché 

                    if k[nb_disque]!=None:
                        for j in k[nb_disque]:

                            if meilleur==j and k["nom"]==nom:
                                k[nb_disque].remove(j)


#4 PROGRAMME PRINCIPAL

import re

print('\033[2J')                                        #pour clear l'affichage et commencer direct 

liste_chronos=[]
liste_scores=[]
turtle.hideturtle()
rejouer=True
passer=turtle.textinput("Bienvenue dans les Tours de Hanoi","Connaissez vous les règles ? (o/n) ")              #demande au joueur si il veut être informé des règles du jeu et des possibilités des aides
while passer not in ["o","n"]:
    passer=turtle.textinput("Bienvenue dans les Tours de Hanoi","Connaissez vous les règles ? (o/n) ")
if passer =='n':
    turtle.textinput("Objectif","Pour gagner vous devez réussir à empiler les disques du plus petit au plus grand sur la tour de droite.")
    turtle.textinput("Règles","Vous pouvez déplacer les disques un par un et un disque ne peut pas être posé sur un disque plus petit que lui. ")
    turtle.textinput("Commandes","Aides : lors de la saisie de la tour de départ vous pouvez : taper -1 pour abandonner ou taper -2 pour revenir au coup précedent")
n=turtle.textinput("Disques","Avec combien de disques voulez vous jouer ? ")
turtle.speed(0)

while not re.match(r'\d', n) or not n.isdigit() or int(n)<1:               #pour empêcher le programme de planter lorsqu'on entre un caractère autre que int ou une quelconque puissance
    n=turtle.textinput("Disques","Nombre de disque invalide. Avec combien de disques voulez vous jouer ? ")

n=int(n)
plateau=init(n)

debut=list(time.localtime())                                                #prend le temps du début du jeu sous forme de liste
for i in range (3):                                                         #enlève les 3 dernières valeurs qui ne nous interressent pas 
    debut.pop()

dessinePlateau(n)
dessineConfig(plateau,n)
victoire,coups,plateau=boucleJeu(plateau,n)
partie=1
liste_scores=[]
liste_chronos=[]
liste_reactions=[]

fin=list(time.localtime())                                              #prend le temps de fin de partie
for i in range (3):                                                     #enlève les 3 dernières valeurs qui ne nous interressent pas 
    fin.pop()    
temps=calcul_temps(debut,fin)

if victoire:
    liste_scores,nom=sauvScore(liste_scores,n,coups)
    liste_chronos=sauvChronos(liste_chronos,n,temps,nom)


re=turtle.textinput("Rejouer","Voulez-vous rejouer ? (o/n) ")                #posibilité de rejouer à l'infini sans relancer le programme
while re not in ["o","n"]:
    re=turtle.textinput("Rejouer","Voulez-vous rejouer ? (o/n) ")
if re=="n":
    rejouer=False
else:
    effaceTout(plateau,n)
    n_1=n
while rejouer :
    import re
    partie+=1
    n=turtle.textinput("Disques","Avec combien de disques voulez vous jouer ? ")
    while not re.match(r'\d', n) or not n.isdigit() or int(n)<1:
        n=turtle.textinput("Disques","Nombre de disque invalide. Avec combien de disques voulez vous jouer ? ")
    n=int(n)
    plateau=init(n)
    if n!=n_1:                                          #si le joueur souhaite refaire une partie avec le même nombre de disques, alors le plateau est conservé car toujours aux bonnes dimensions
        turtle.reset()
        turtle.hideturtle()
        turtle.speed(0)
        dessinePlateau(n)

    else:                                            #sinon le plateau est retracé pour être adapté à la taille des disques 
        effaceTout(plateau,n)

    debut=list(time.localtime())                                                #prend le temps du début du jeu sous forme de liste
    for i in range (3):                                                         #enlève les 3 dernières valeurs qui ne nous interressent pas 
        debut.pop()

    dessineConfig(plateau,n)

    victoire,coups,plateau=boucleJeu(plateau,n)
    
    fin=list(time.localtime())                                              #prend le temps de fin de partie
    for i in range (3):                                                     #enlève les 3 dernières valeurs qui ne nous interressent pas 
        fin.pop()    
    temps=calcul_temps(debut,fin)

    if victoire:
        liste_scores,nom=sauvScore(liste_scores,n,coups)
        liste_chronos=sauvChronos(liste_chronos,n,temps,nom)
    re=turtle.textinput("Rejouer","Voulez-vous rejouer ? (o/n) ")
    while re not in ["o","n"]:
        re=turtle.textinput("Rejouer","Voulez-vous rejouer ? (o/n) ")
    if re=="n":
        rejouer=False
    else:
        effaceTout(plateau,n)
    n_1=n

if liste_scores!=[]:                                    #si il n'y a pas de partie de gagné on ne peut pas voir de scores
    tableau=turtle.textinput("Classement","Voulez vous voir les meilleurs scores ? (o/n)")  #demande au joueur s'il veut avoir le classement
    while tableau not in ["o","n"]:
        tableau=turtle.textinput("Classement","Voulez vous voir les meilleurs scores ? (o/n)")
    if tableau=="o":
        sc=turtle.textinput("Disque","Pour les parties avec combien de disques voulez vous voir le classement ?")

        import re
        while not re.match(r'\d', sc) or not sc.isdigit():
            sc=turtle.textinput("Disque","Pour les parties avec combien de disques voulez vous voir le classement ?")

        a=afficheScores(liste_scores,int(sc))
        while a==0:
            sc=turtle.textinput("Disque","Auncune partie n'a été faite avec de nombre de disque, pour les parties avec combien de disques voulez vous voir le classement ?")

            while not re.match(r'\d', sc) or not sc.isdigit():
                sc=turtle.textinput("Disque","Auncune partie n'a été faite avec de nombre de disque, pour les parties avec combien de disques voulez vous voir le classement ?")
            a=afficheScores(liste_scores,int(sc))
        afficheChronos(liste_chronos,int(sc))
turtle.textinput("Merci d'avoir joué","À bientôt :)")
