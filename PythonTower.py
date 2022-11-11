"""Tower est un jeu développé par Ptitloup(c'est moi ^^)"""

"""Bienvenue sur le jeu Tower en Version 1.2.0"""

####1.3.0:plus d'animation et de plus beau décor
#1.4.0:un système de combat intéractif et déplacement du personnage

import sys
import  pygame
import random as rd

pygame.init()

DicoVariable={
    'Heros':{'Nom':'Heros','Vie':100,'VieMax':100,'Mana':10,'ManaMax':10,'RegenerationMana':1,
        'Etage':1,'EtageObjet':10,'Degat':0,'Niveau':1,'Experience':0,'ExperienceNecessaire':10,'Or':0,
        'BonusForce':0,'BonusVie':0,'BonusMana':0,'ChanceCoupCritique':0,'Puissance':0,
        'Potion':1,'Fiole':1,'Bombe':0,'VieRecuperee':0},
    'Boss':{'Vie':0,'Force':0,'Grade':(0,0,1,0,2,0,0,1,2,3),'BonusGrade':(-40,-10,20,50),'NomGrade':('Sbire','GrosBras','SousBoss','Boss')}}

ObjetTower={
    'Arme':('Dague de Vampirisme','Baton de Mage','Epee de Paladin'),
    'Armure':('Armure d\'Epine','Cape de Voleur','Armure de Paladin'),
    'Artefact':('Talisman de Pouvoir','Plume de Phoenix','Casque de Paladin')}

ObjetHeros={'Arme':['epee en fer'],'Armure':['armure en cuir'],'Artefact':['anneau en cuivre']}

ListeSorts=('Explosion (6)','Vol de vie (10)','Magie Noire (X)','Annuler')

ListeDecor=('Trou_dans_le_mur_nuit','Fenetre_nuit','Poutre')

ListeBoss={'Sbire':['LeBoss'],'GrosBras':['LeBoss'],'SousBoss':['LeBoss'],'Boss':['LeBoss']}

timer=False

sizescreen= weight,length = 720,580
screen=pygame.display.set_mode(sizescreen)
police=pygame.freetype.SysFont("Arial",12)


background = pygame.image.load("Image tower/BackDetaile.PNG")
fondunoir = pygame.image.load("Image tower/FonduNoir.PNG")
heros = pygame.image.load("Image tower/LeHerosDetaile.png")
arme = pygame.image.load("Image tower/Objet/image/epee en fer.png")
armure = pygame.image.load("Image tower/Objet/image/armure en cuir bras baisse.png")
artefact = pygame.image.load("Image tower/Objet/image/anneau en cuivre.png")
boss = pygame.image.load("Image tower/"+ListeBoss['Sbire'][rd.randint(0,len(ListeBoss['Sbire'])-1)]+".PNG")
decor = pygame.image.load("Image tower/Decor/"+ListeDecor[rd.randint(0,len(ListeDecor)-1)]+'.PNG')
frappe = pygame.image.load('Image tower/frappe.PNG')
hud = pygame.image.load('Image tower/HUD.PNG')

def animation_frapper():
    for i in range(1,10):
        screen.blit(background, (0,0))
        screen.blit(decor, (240, 0))
        screen.blit(heros, (25+i*10,205))
        screen.blit(arme, (25+i*10,205))
        screen.blit(armure, (25+i*10, 205))
        screen.blit(artefact, (25+i*10, 205))
        screen.blit(boss, (460+i,110))
        screen.blit(frappe,(500,170))
        pygame.display.flip()
        pygame.time.delay(10)
    affichageEcran()
    affichageHUD()
    pygame.display.flip()
    return

def animation_sortdegat():
    armure = pygame.image.load("Image tower/Objet/Image/" + str(ObjetHeros['Armure'][0]) + " bras baisse.PNG")
    for i in range(1,7):
        heros = pygame.image.load("Image tower/Animation/Sort de degat/"+str(i)+'.png')
        screen.blit(background, (0,0))
        screen.blit(decor, (240,0))
        screen.blit(heros, (25,205))
        screen.blit(arme, (25, 205))
        screen.blit(armure, (25, 205))
        screen.blit(artefact, (25, 205))
        screen.blit(boss, (460+i,110))
        pygame.display.flip()
        pygame.time.delay(50)
        armure = pygame.image.load("Image tower/Objet/Image/" + str(ObjetHeros['Armure'][0]) + " bras leve.PNG")
    affichageEcran()
    affichageHUD()
    pygame.display.flip()
    return

def animation_potion_Soin():
    armure = pygame.image.load("Image tower/Objet/Image/" + str(ObjetHeros['Armure'][0]) + " bras baisse.PNG")
    for i in range(1, 7):
        heros = pygame.image.load("Image tower/Animation/AnimationPotionSoin/" + str(i) + '.png')
        screen.blit(background, (0, 0))
        screen.blit(decor, (240, 0))
        screen.blit(heros, (25, 205))
        screen.blit(arme, (25, 205))
        screen.blit(armure, (25, 205))
        screen.blit(artefact, (25, 205))
        screen.blit(boss, (460 + i, 110))
        pygame.display.flip()
        pygame.time.delay(50)
        armure = pygame.image.load("Image tower/Objet/Image/" + str(ObjetHeros['Armure'][0]) + " bras leve.PNG")
    affichageEcran()
    affichageHUD()
    pygame.display.flip()

def animation_potion_Mana():
    armure = pygame.image.load("Image tower/Objet/Image/" + str(ObjetHeros['Armure'][0]) + " bras baisse.PNG")
    for i in range(1, 7):
        heros = pygame.image.load("Image tower/Animation/AnimationPotionMana/" + str(i) + '.png')
        screen.blit(background, (0, 0))
        screen.blit(decor, (240, 0))
        screen.blit(heros, (25, 205))
        screen.blit(arme, (25, 205))
        screen.blit(armure, (25, 205))
        screen.blit(artefact, (25, 205))
        screen.blit(boss, (460 + i, 110))
        pygame.display.flip()
        pygame.time.delay(50)
        armure = pygame.image.load("Image tower/Objet/Image/" + str(ObjetHeros['Armure'][0]) + " bras leve.PNG")
    affichageEcran()
    affichageHUD()
    pygame.display.flip()

def ConversionVariableImage(Variable,Position):
    ListedeCaractere=list(str(abs(Variable)))
    for i in range(3-len(ListedeCaractere)):ListedeCaractere=['0']+ListedeCaractere
    X,Y=Position
    for indice in range(len(ListedeCaractere)):
        Caractere=pygame.image.load('Image tower/Chiffre/Numero'+ListedeCaractere[indice]+'.PNG')
        screen.blit(Caractere,(X+indice*7,Y))

def fondu_au_noir():
    screen.blit(fondunoir,(0,0))
    pygame.display.flip()

def affichageEcran():
    screen.blit(background, (0, 0))
    screen.blit(decor, (240, 0))
    screen.blit(heros, (25, 205))
    screen.blit(arme, (25,205))
    screen.blit(armure, (25, 205))
    screen.blit(artefact, (25, 205))
    screen.blit(boss, (460, 110))
    pygame.display.update()

def affichageBulleSort(curseur):
    Arrow = pygame.image.load("Image tower/ArrowSort.PNG")
    Box = pygame.image.load("Image tower/SpellBox.PNG")
    screen.blit(Box, (100, 180))
    screen.blit(Arrow,(97,200+curseur * 15))
    screen.blit(police.render('Sort :', (255, 255, 255))[0], (110,190))
    for i in range(len(list(ListeSorts))):
        screen.blit(police.render((str(list(ListeSorts)[i])), (255, 255, 255))[0], (120, 205 + i * 15))
    pygame.display.update()

def affichageBullInventaire(curseur):
    Arrow = pygame.image.load('Image tower/ArrowItem.PNG')
    Box = pygame.image.load('Image tower/ItemBox.PNG')
    screen.blit(Box,(100,180))
    screen.blit(Arrow,(97,197+curseur * 15))
    inventaire_tpl1 = police.render('L\'inventaire :', (255, 255, 255))
    screen.blit(inventaire_tpl1[0], (110, 190))
    inventaire_tpl2 = police.render('D: Potions: ' + str(DicoVariable['Heros']['Potion']), (255, 255, 255))
    screen.blit(inventaire_tpl2[0], (120, 205))
    inventaire_tpl3 = police.render('Q: Fioles: ' + str(DicoVariable['Heros']['Fiole']), (255, 255, 255))
    screen.blit(inventaire_tpl3[0], (120, 220))
    inventaire_tpl4 = police.render('Z: Bombe: ' + str(DicoVariable['Heros']['Bombe']), (255, 255, 255))
    screen.blit(inventaire_tpl4[0], (120, 235))
    inventaire_tpl5 = police.render('Retour', (255, 255, 255))
    screen.blit(inventaire_tpl5[0], (120, 250))
    pygame.display.update()

def ChoixAction():
    BoxChoix = 1
    Box = pygame.image.load('Image tower/Animation/ChoixAction/1.PNG')
    screen.blit (Box,(25,205))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    for i in (0,0):
                        BoxChoix-=1
                        if BoxChoix == 0: BoxChoix = 6
                        Box = pygame.image.load('Image tower/Animation/ChoixAction/'+str(BoxChoix)+'.PNG')
                        affichageEcran()
                        screen.blit(Box, (25, 205))
                        pygame.display.update()
                        pygame.time.delay(50)
                if event.key == pygame.K_d:
                    for i in (0, 0):
                        BoxChoix += 1
                        if BoxChoix == 7: BoxChoix = 1
                        Box = pygame.image.load('Image tower/Animation/ChoixAction/' + str(BoxChoix) + '.PNG')
                        affichageEcran()
                        screen.blit(Box, (25, 205))
                        pygame.display.update()
                        pygame.time.delay(50)
                if event.key == pygame.K_e:
                    return BoxChoix

def affichageHUD():
    screen.blit(hud,(0,480))
    ConversionVariableImage(DicoVariable['Heros']['Vie'],(24,493))
    ConversionVariableImage(DicoVariable['Heros']['VieMax'],(52,493))
    ConversionVariableImage(DicoVariable['Heros']['Mana'],(24,510))
    ConversionVariableImage(DicoVariable['Heros']['ManaMax'],(52,510))
    ConversionVariableImage(DicoVariable['Heros']['Experience'],(24,527))
    ConversionVariableImage(DicoVariable['Heros']['ExperienceNecessaire'],(52,527))
    ConversionVariableImage(DicoVariable['Boss']['Vie'],(125,493))
    ConversionVariableImage(DicoVariable['Heros']['Etage'],(125,510))
    ConversionVariableImage(DicoVariable['Heros']['Niveau'],(125,527))
    ConversionVariableImage(DicoVariable['Heros']['Or'],(125,544))
    Arme=pygame.image.load('Image tower/Objet/item/'+ObjetHeros['Arme'][0]+'.PNG')
    screen.blit(Arme,(78,489))
    Armure=pygame.image.load('Image tower/Objet/item/'+ObjetHeros['Armure'][0]+'.PNG')
    screen.blit(Armure,(78,517))
    Artefact=pygame.image.load('Image tower/Objet/item/'+ObjetHeros['Artefact'][0]+'.PNG')
    screen.blit(Artefact,(78,545))
    pygame.display.update()
    
def Shop():
    global DicoVariable
    affichageHUD()
    timer=False
    while timer == False:
        tpl_shop1= police.render('Vous pouvez acheter des objets',(255,255,255))
        screen.blit(tpl_shop1[0],(160,500))
        tpl_shop2= police.render('D:Potion: 100G Q:Fiole: 100G Z:Bombe: 500G S:retour',(255,255,255))
        screen.blit(tpl_shop2[0],(160,520))
        pygame.display.update()
        tpl_shop3 = police.render('retour', (255, 255, 255))
        for shop_event in pygame.event.get():
            if shop_event.type == pygame.KEYDOWN:
                if shop_event.key == pygame.K_z:
                    if DicoVariable['Heros']['Or']>=500:
                        tpl_shop3 = police.render('Bombe achetée', (255, 255, 255))
                        DicoVariable['Heros']['Or']-=500
                        DicoVariable['Heros']['Bombe']+=1
                    else:tpl_shop3=police.render('Vous n\'avez pas d\'argent',(255,255,255))
                if shop_event.key == pygame.K_q:
                    if DicoVariable['Heros']['Or'] >= 100:
                        tpl_shop3 = police.render('Fiole achetée', (255, 255, 255))
                        DicoVariable['Heros']['Or'] -= 100
                        DicoVariable['Heros']['Fiole']+=1
                    else:tpl_shop3=police.render('Vous n\'avez pas d\'argent',(255,255,255))
                if shop_event.key == pygame.K_d:
                    if DicoVariable['Heros']['Or'] >= 100:
                        tpl_shop3 = police.render('Potion achetée', (255, 255, 255))
                        DicoVariable['Heros']['Or'] -= 100
                        DicoVariable['Heros']['Potion']+=1
                    else:tpl_shop3=police.render('Vous n\'avez pas d\'argent',(255,255,255))
                if shop_event.key == pygame.K_s:
                    timer=True
                affichageHUD()
                screen.blit(tpl_shop3[0],(160,500))
                pygame.display.update()
                pygame.time.delay(350)
                affichageHUD()

def EffetArmure(Armure):
    global DicoVariable
    DegatReduit=0
    if Armure == 'armure en cuir' : DegatReduit = 0
    if Armure == 'Armure de Paladin' : DegatReduit = 3
    if Armure == 'Armure d\'Epine' :
        DegatReduit=1
        DicoVariable['Boss']['Vie']-=rd.randint(2,5)
    if Armure == 'Cape de Voleur' :
        DegatReduit=0
        DicoVariable['Heros']['Or']+=rd.randint(0,20)
    if ObjetHeros['Artefact'][0] == 'Casque de Paladin' : DegatReduit+=3
    return DegatReduit

def EffetArme(Arme,TypeAttaque):
    global DicoVariable
    DegatBonus=0
    if TypeAttaque == 'Attaque Physique' :
        DegatBonus=0
        if Arme == 'epee en fer' : DegatBonus = 0
        if Arme == 'Epee de Paladin' : DegatBonus = 10
        if Arme == 'Dague de Vampirisme' :
            DegatBonus= 3
            DicoVariable['Heros']['VieRecuperee']+=rd.randint(3,7)
    if TypeAttaque == 'Attaque Magique' :
        DegatBonus=0
        if Arme == 'Baton de Mage' : DegatBonus = 25

        if ObjetHeros['Artefact'][0] == 'Talisman de puissance' : DegatBonus+=rd.randint(10,30)

    return DegatBonus

###Debut du code

affichageEcran()
affichageHUD()

running = True
while DicoVariable['Heros']['Etage']<=100 and running:
    EtageModulo10=DicoVariable['Heros']['Etage']
    while EtageModulo10>=11: EtageModulo10-=10
    BonusVieBoss=DicoVariable['Boss']['BonusGrade'][DicoVariable['Boss']['Grade'][EtageModulo10-1]]
    boss = pygame.image.load("Image tower/"+ListeBoss[DicoVariable['Boss']['NomGrade'][DicoVariable['Boss']['Grade'][EtageModulo10-1]]][rd.randint(0,len(ListeBoss[DicoVariable['Boss']['NomGrade'][DicoVariable['Boss']['Grade'][EtageModulo10-1]]])-1)]+".PNG")
    DicoVariable['Boss']['Vie']=rd.randint(100,200)+BonusVieBoss
    affichageHUD()
    affichageEcran()
    while DicoVariable['Boss']['Vie']>0 and running:
        action=True
        Choix = ChoixAction()
###Action du joueur

#Frapper

        if Choix == 1 and action == True:
            DegatBonus=EffetArme(ObjetHeros['Arme'][0],'Attaque Physique')
            dice100=rd.randint(1,100)
            if dice100<DicoVariable['Heros']['ChanceCoupCritique']:
                DegatBonus*=3
                screen.blit(police.render('Coup Critique', (255, 255, 255))[0], (155, 500))
                pygame.display.update()
            DicoVariable['Boss']['Vie']-=rd.randint(10,20)+DegatBonus+DicoVariable['Heros']['BonusForce']
            if DicoVariable['Boss']['Vie']<0:DicoVariable['Boss']['Vie']=0
            DicoVariable['Heros']['Mana']+=1
            if DicoVariable['Heros']['Mana']>DicoVariable['Heros']['ManaMax']:DicoVariable['Heros']['Mana']=DicoVariable['Heros']['ManaMax']
            animation_frapper()
            action = False
#Utiliser de la magie
        if Choix==5 and action==True:
            affichageHUD()
            curseur=0
            affichageBulleSort(curseur)
            timer=False
            while timer == False:
                for spell_event in pygame.event.get():
                    if spell_event.type == pygame.KEYDOWN:
                        if spell_event.key == pygame.K_z : curseur -= 1
                        if spell_event.key == pygame.K_s : curseur += 1
                        if spell_event.key == pygame.K_e : timer = True
                        if curseur<=-1:curseur=0
                        if curseur>=4:curseur=3
                    affichageBulleSort(curseur)
            if curseur==0:
                if DicoVariable['Heros']['Mana'] >= 6:
                    DicoVariable['Heros']['Mana'] -= 6
                    DegatBonus = EffetArme(ObjetHeros['Arme'][0], 'Attaque Magique')
                    DicoVariable['Boss']['Vie'] -= rd.randint(90, 110) + DegatBonus
                    animation_sortdegat()
                    action=False
            if curseur==1:
                if DicoVariable['Heros']['Mana'] >= 10:
                    DicoVariable['Heros']['Mana'] -= 10
                    DegatBonus = EffetArme(ObjetHeros['Arme'][0], 'Attaque Magique')
                    DicoVariable['Boss']['Vie'] -= rd.randint(50, 90) + DegatBonus + DicoVariable['Heros']['Puissance']
                    DicoVariable['Heros']['Vie'] += rd.randint(25, 45)
                    action = False
            if curseur==2:
                if DicoVariable['Heros']['Mana'] >= 1:
                    DegatBonus = EffetArme(ObjetHeros['Arme'][0], 'Attaque Magique')
                    ManaCost=DicoVariable['Heros']['Mana']
                    DicoVariable['Boss']['Vie'] -= rd.randint(5*ManaCost,15*ManaCost) + DegatBonus + DicoVariable['Heros']['Puissance']
                    DicoVariable['Heros']['Vie'] -= rd.randint(ManaCost,2*ManaCost)
                    DicoVariable['Heros']['Mana']=0
                    action = False
            affichageHUD()
            affichageEcran()
        if DicoVariable['Boss']['Vie']<0:DicoVariable['Boss']['Vie']=0
#Utiliser son inventaire
        if Choix == 3 and action == True:
            affichageHUD()
            curseur=0
            affichageBullInventaire(curseur)
            inventaire_tpl5=police.render('retour',(255,255,255))
            timer=False
            while timer == False:
                for item_event in pygame.event.get():
                    if item_event.type == pygame.KEYDOWN:
                        if item_event.key == pygame.K_z : curseur-=1
                        if item_event.key == pygame.K_s : curseur+=1
                        if item_event.key == pygame.K_e : timer=True
                        if curseur<=-1:curseur=0
                        if curseur>=4:curseur=3
                    affichageBullInventaire(curseur)
            if curseur == 2:
                if DicoVariable['Heros']['Bombe'] >= 1:
                    DicoVariable['Heros']['Bombe'] -= 1
                    DicoVariable['Boss']['Vie'] -= 200
                    inventaire_tpl5 = police.render('Bombe utilisée', (255, 255, 255))
                    action = False
                else:
                    inventaire_tpl5 = police.render('pas de Bombe', (255, 255, 255))
            if curseur == 0:
                if DicoVariable['Heros']['Potion'] >= 1:
                    DicoVariable['Heros']['Potion'] -= 1
                    DicoVariable['Heros']['Vie'] += 80
                    animation_potion_Soin()
                    inventaire_tpl5 = police.render('Potion utilisée', (255, 255, 255))
                    action = False
                else:
                    inventaire_tpl5 = police.render('pas de Potion', (255, 255, 255))
            if curseur == 1:
                if DicoVariable['Heros']['Fiole'] >= 1:
                    DicoVariable['Heros']['Fiole'] -= 1
                    DicoVariable['Heros']['Mana'] += 8
                    animation_potion_Mana()
                    inventaire_tpl5 = police.render('Fiole utilisée', (255, 255, 255))
                    action = False
                else:
                    inventaire_tpl5 = police.render('pas de Fiole', (255, 255, 255))
            affichageEcran()
            affichageHUD()
            screen.blit(inventaire_tpl5[0],(160,500))
            pygame.display.update()

###Attribuer les dégats

            if DicoVariable['Heros']['Vie']>DicoVariable['Heros']['VieMax']:DicoVariable['Heros']['Vie']=DicoVariable['Heros']['VieMax']
            if DicoVariable['Heros']['Mana']>DicoVariable['Heros']['ManaMax']:DicoVariable['Heros']['Mana']=DicoVariable['Heros']['ManaMax']
            DegatReduit=EffetArmure(ObjetHeros['Armure'][0])
            if action == False:
                DicoVariable['Heros']['Vie']-=rd.randint(3,7)-DegatReduit+DicoVariable['Boss']['Force']
                action = True
        if DicoVariable['Heros']['Vie']<=0:
            if 'Plume de Phoenix' in ObjetHeros['Artefact']:
                ObjetHeros['Artefact'],DicoVariable['Heros']['Vie']=['anneau en cuivre'],DicoVariable['Heros']['VieMax']
                tpl=police.render('La plume vous a protégé de la mort',(255,255,255))
                screen.blit(tpl[0],(160,500))
                pygame.display.update()
            else:
                fondu_au_noir()
                affichageHUD()
                tpl=police.render(str(DicoVariable['Heros']['Nom'])+' est mort',(255,255,255))
                screen.blit(tpl[0],(160,500))
                pygame.display.update()
                running = False
                break

### Monter D'un étage

    fondu_au_noir()
    pygame.time.delay(150)
    DicoVariable['Heros']['Or']+=rd.randint(10,30)
    DicoVariable['Heros']['Etage']+=1
    DicoVariable['Heros']['Vie']+=rd.randint(0,10)+DicoVariable['Heros']['VieRecuperee']
    DicoVariable['Heros']['VieRecuperee']=0
    decor = pygame.image.load("Image tower/Decor/" + ListeDecor[rd.randint(0, len(ListeDecor) - 1)] + '.PNG')
# Le shop
    if rd.randint(0,25)==0:
        Shop()
# Gagner un objet
    if DicoVariable['Heros']['Etage']==DicoVariable['Heros']['EtageObjet']:
        DicoVariable['Heros']['EtageObjet']+=10
        DicoVariable['Heros']['RegenerationMana']+=1
        DicoVariable['Boss']['Force']+=3
        lvl_tpl1=police.render('Vous pouvez choisir un objet:',(255,255,255))
        screen.blit(lvl_tpl1[0],(160,500))
        pygame.display.update()
        ListeObjetTrouve={X:[] for X in ObjetTower.keys()}
        for i in ObjetTower.keys():
            timer = False
            while timer==False:
                Objet=rd.randint(0,(len(ObjetTower[i]))-1)
                if not(ObjetTower[i][Objet] in ObjetHeros[i]) and not(ObjetTower[i][Objet] in ListeObjetTrouve[i]):
                    ListeObjetTrouve[i].append(ObjetTower[i][Objet])
                    timer = True
        item_tpl=police.render('Q: '+ str(ListeObjetTrouve['Artefact']) +' D: ' +str(ListeObjetTrouve['Armure'])+' Z: '+str(ListeObjetTrouve['Arme']),(255,255,255))
        screen.blit(item_tpl[0],(160,520))
        pygame.display.update()
        timer=False
        while timer == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        ObjetHeros['Arme']=ListeObjetTrouve['Arme']
                        arme = pygame.image.load("Image tower/Objet/image/"+str(ObjetHeros['Arme'])+'.png')
                    if event.key == pygame.K_d:
                        ObjetHeros['Armure']=ListeObjetTrouve['Armure']
                        armure = pygame.image.load("Image tower/Objet/image/" + str(ObjetHeros['Armure']) + 'bras baisse.png')
                    if event.key == pygame.K_q:
                        ObjetHeros['Artefact']=ListeObjetTrouve['Artefact']
                        artefact = pygame.image.load("Image tower/Objet/image/" + str(ObjetHeros['Artefact']) + '.png')
                    timer=True
                    affichageHUD()
    if DicoVariable['Heros']['Vie']>DicoVariable['Heros']['VieMax']:DicoVariable['Heros']['Vie']=DicoVariable['Heros']['VieMax']
    DicoVariable['Heros']['Experience']+=rd.randint(3,7)
# Gagner un niveau
    if DicoVariable['Heros']['Experience']>=DicoVariable['Heros']['ExperienceNecessaire']:
        DicoVariable['Heros']['Experience'],DicoVariable['Heros']['Vie'],timer=0,DicoVariable['Heros']['VieMax'],False
        DicoVariable['Heros']['Niveau']+=1
        DicoVariable['Heros']['ExperienceNecessaire']=10*DicoVariable['Heros']['Niveau']
        up_tpl1=police.render('Votre niveau augmente, vous pouvez choisir une compétance à améliorer',(255,255,255))
        screen.blit(up_tpl1[0],(160,500))
        up_tpl2=police.render('(z) Force , (q) Magie ,(d) Vie',(255,255,255))
        screen.blit(up_tpl2[0],(160,520))
        pygame.display.update()
        up_tpl3=police.render('Vous n\'avez rien augmenter',(255,255,255))
        while timer==False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        DicoVariable['Heros']['BonusForce']+=2
                        DicoVariable['Heros']['ChanceCoupCritique']+=10
                        timer=True
                        up_tpl3=police.render('vous gagnez de la force',(255,255,255))
                    if event.key == pygame.K_d:
                        DicoVariable['Heros']['BonusVie']+=5
                        DicoVariable['Heros']['VieMax']+=DicoVariable['Heros']['BonusVie']
                        DicoVariable['Heros']['Vie']=DicoVariable['Heros']['VieMax']
                        timer=True
                        up_tpl3=police.render('vous gagnez de la vie',(255,255,255))
                    if event.key == pygame.K_q:
                        DicoVariable['Heros']['BonusMana']+=1
                        DicoVariable['Heros']['ManaMax']+=DicoVariable['Heros']['BonusMana']
                        DicoVariable['Heros']['Mana']=DicoVariable['Heros']['ManaMax']
                        DicoVariable['Heros']['Puissance']+=10
                        timer=True
                        up_tpl3=police.render('vous gagnez du mana',(255,255,255))
                    screen.blit(up_tpl3[0],(160,500))
                pygame.display.update()

###La fin

affichageHUD()
if running == True: end_tpl=police.render("Vous avez gagné",(255,255,255))
else: end_tpl=police.render("Vous avez perdu",(255,255,255))
screen.blit(end_tpl[0],(160,500))
pygame.display.update()
pygame.time.delay(1000)