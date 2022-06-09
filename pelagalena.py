import random

Mazzo_giocatoreA = ['1', '2', '3', '4', '5', '6', '7', 'F', 'C', 'R', '1', '2', '3', '4', '5', '6', '7', 'F', 'C', 'R',]

Mazzo_giocatoreB = ['1', '2', '3', '4', '5', '6', '7', 'F', 'C', 'R', '1', '2', '3', '4', '5', '6', '7', 'F', 'C', 'R',]

Carte_in_gioco = [ ]

ULTIMA_PRESA = 0

AZIONE = 0

numero = 0

def ASSEGNAA():
    for a in range (0, int(str(len(Mazzo_giocatoreA)))): 
        if 'B' in Mazzo_giocatoreA[a] and len(Mazzo_giocatoreA[a])==2:
            Mazzo_giocatoreA[a] = Mazzo_giocatoreA[a].replace('B','A')
        elif len(Mazzo_giocatoreA[a])<2:
            Mazzo_giocatoreA[a] = Mazzo_giocatoreA[a]+'A'
def ASSEGNAB():
    for a in range (0, int(str(len(Mazzo_giocatoreB)))): 
        if 'A' in Mazzo_giocatoreB[a] and len(Mazzo_giocatoreB[a])==2:
            Mazzo_giocatoreB[a] = Mazzo_giocatoreB[a].replace('A','B')
        elif len(Mazzo_giocatoreB[a])<2:
            Mazzo_giocatoreB[a] = Mazzo_giocatoreB[a]+'B'
def ASSEGNATUTTO():
    ASSEGNAA()
    ASSEGNAB()
def PRINT_GAME():
    global numero
    print('____________________________________________')
    print("mossa", numero, "\nULTIMA PRESA: ", ULTIMA_PRESA)
    numero = numero +1
    print("AZIONE: ", AZIONE)
    print('\n+.+.+.+.+.+.+.+.+.+')
    print('\n☺A →' + str(Mazzo_giocatoreA))
    print('█ →' + str(Carte_in_gioco))
    print('☺B →' + str(Mazzo_giocatoreB))
def METTEA():
    Carte_in_gioco.insert(0, Mazzo_giocatoreA[0])
    Mazzo_giocatoreA.remove(Mazzo_giocatoreA[0])
    PRINT_GAME()
    CAMBIA_AZIONE()
def METTEB():
    Carte_in_gioco.insert(0, Mazzo_giocatoreB[0])
    Mazzo_giocatoreB.remove(Mazzo_giocatoreB[0])
    PRINT_GAME()
    CAMBIA_AZIONE()
def PRENDEA():
    global Mazzo_giocatoreA
    global ULTIMA_PRESA
    global AZIONE
    Carte_in_gioco.reverse()
    Mazzo_giocatoreA= Mazzo_giocatoreA + Carte_in_gioco
    Carte_in_gioco.clear()
    ULTIMA_PRESA="A"
    AZIONE=0
    ASSEGNATUTTO()
    PRINT_GAME()
def PRENDEB():
    global Mazzo_giocatoreB
    global ULTIMA_PRESA
    global AZIONE
    Carte_in_gioco.reverse()
    Mazzo_giocatoreB = Mazzo_giocatoreB + Carte_in_gioco
    Carte_in_gioco.clear()
    ULTIMA_PRESA="B"
    AZIONE=0
    ASSEGNATUTTO()
    PRINT_GAME()
def CAMBIA_AZIONE():
    global AZIONE
    global Carte_in_gioco
    if Carte_in_gioco[0] == "1B":
        AZIONE = "A_deve_mettere_1_carta"
        METTEA()
    elif Carte_in_gioco[0] == "1A":
        AZIONE = "B_deve_mettere_1_carta"
        METTEB()
    elif Carte_in_gioco[0] == "2B":
        AZIONE = "A_deve_mettere_2_carte"
        METTEA()
    elif Carte_in_gioco[0] == "2A":
        AZIONE = "B_deve_mettere_2_carte"
        METTEB()
    elif Carte_in_gioco[0] == "3B":
        AZIONE = "A_deve_mettere_3_carte"
        METTEA()
    elif Carte_in_gioco[0] == "3A":
        AZIONE = "B_deve_mettere_3_carte"
        METTEB()
    else:
        if AZIONE == 0 and "B" in str(Carte_in_gioco[0]):
            METTEA()
        elif AZIONE == 0 and "A" in str(Carte_in_gioco[0]):
            METTEB()
        elif AZIONE == "A_deve_mettere_1_carta":
            PRENDEB()
        elif AZIONE == "B_deve_mettere_1_carta":
            PRENDEA()
        elif AZIONE == "A_deve_mettere_2_carte":
            AZIONE = "A_deve_mettere_1_carta"
            METTEA()
        elif AZIONE == "B_deve_mettere_2_carte":
            AZIONE = "B_deve_mettere_1_carta"
            METTEB()
        elif AZIONE == "A_deve_mettere_3_carte":
            AZIONE = "A_deve_mettere_2_carte"
            METTEA()
        elif AZIONE == "B_deve_mettere_3_carte":
            AZIONE = "B_deve_mettere_2_carte"
            METTEB()
    
#1. INIZIO
print("BENVENUTO AL SIMULATORE DI PARTITE POSSIBILI A PELA GALÈNA")
print("- il giocatore che inizia la partita è scelto in modo casuale")
mescolo=input("- le carte nei mazzi hanno un ordine di default, vuoi mescolarle? digita s/n → ")
if mescolo == "s":
    random.shuffle(Mazzo_giocatoreA)
    random.shuffle(Mazzo_giocatoreB)
    ASSEGNATUTTO()
    PRINT_GAME()
elif mescolo == "n":
    ASSEGNATUTTO()
    PRINT_GAME()

else: print("ERRORE, CAPRONE!")
        
            
#1.1 Mescolamento dei mazzi


while len(Mazzo_giocatoreB)!=0 and len(Mazzo_giocatoreB)!=0:
    try:
        if AZIONE == 0 and ULTIMA_PRESA == 0:
            ASSEGNATUTTO()
            scelte=["a", "b"]
            dado = random.choice(scelte)
            if dado=="a":
                METTEA()
            else:
                METTEB()
            
        while ULTIMA_PRESA != 0:
            if ULTIMA_PRESA =="A":
                ASSEGNATUTTO()
                METTEA()
            elif ULTIMA_PRESA =="B":
                ASSEGNATUTTO()
                METTEB()

    except IndexError:
        print ("\n - il gioco è finito, andate in pace - ")
        if len(Mazzo_giocatoreA)==0:
            print('\nQuella gallina del giocatore A è stata pelata')
        elif len(Mazzo_giocatoreB)==0:
            print('\nQuella gallina del giocatore B è stata pelata')
        break
