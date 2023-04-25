import random


Mazzo_giocatoreA=[]
Mazzo_giocatoreB=[]
Mazzo_intero=[]
Carte_in_gioco=[]
ULTIMA_PRESA=0
salva_A=[]
salva_B=[]
AZIONE=0
numero=0
#impostazione foglio


def lettura_finale(m,v):
    with open("big.txt","a",encoding='utf-16') as doc: 
        if m>1000:
            doc.write(str(m)+",")
            doc.write(str(v))
            doc.write("\n")
        #print("salvato")
        doc.close()


 

def lettore(a,b,m):
    with open("big.txt","a",encoding='utf-16') as doc:
        if m>1000:
            for i in a:
                doc.write(i+",")
            for i in b:
                doc.write(i+",")
        doc.close()
        #print("salvato")



def ASSEGNAA():
    global Mazzo_giocatoreA
    for a in range (0, len(Mazzo_giocatoreA)): 
        if 'B' in Mazzo_giocatoreA[a] and len(Mazzo_giocatoreA[a])==2:
            Mazzo_giocatoreA[a] = Mazzo_giocatoreA[a].replace('B','A')
        elif len(Mazzo_giocatoreA[a])<2:
            Mazzo_giocatoreA[a] = Mazzo_giocatoreA[a]+'A'
def ASSEGNAB():
    global Mazzo_giocatoreB
    for a in range (0, len(Mazzo_giocatoreB)): 
        if 'A' in Mazzo_giocatoreB[a] and len(Mazzo_giocatoreB[a])==2:
            Mazzo_giocatoreB[a] = Mazzo_giocatoreB[a].replace('A','B')
        elif len(Mazzo_giocatoreB[a])<2:
            Mazzo_giocatoreB[a] = Mazzo_giocatoreB[a]+'B'
def ASSEGNATUTTO():
    global Mazzo_giocatoreB
    global Mazzo_giocatoreA
    ASSEGNAA()
    ASSEGNAB()
def PRINT_GAME():
    global numero
    #print('____________________________________________')
    #print("mossa", numero, "\nULTIMA PRESA: ", ULTIMA_PRESA)
    numero = numero +1
    #print("AZIONE: ", AZIONE)
    #print('\n+.+.+.+.+.+.+.+.+.+')
    #print('\n☺A →' + str(Mazzo_giocatoreA))
    #print('█ →' + str(Carte_in_gioco))
    #print('☺B →' + str(Mazzo_giocatoreB))
def METTEA():
    Carte_in_gioco.insert(0, str(Mazzo_giocatoreA[0]))
    Mazzo_giocatoreA.remove(Mazzo_giocatoreA[0])
    PRINT_GAME()
    CAMBIA_AZIONE()
def METTEB():
    Carte_in_gioco.insert(0, str(Mazzo_giocatoreB[0]))
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

def GIOCO():
    global Mazzo_giocatoreA
    global Mazzo_giocatoreB
    global Mazzo_intero
    global salva_A
    global salva_B
    global Carte_in_gioco
    global ULTIMA_PRESA
    global AZIONE
    global numero
    Mazzo_giocatoreA.clear()
    Mazzo_giocatoreB.clear()
    Mazzo_intero.clear()
    Mazzo_giocatoreA = ['1', '2', '3', '0', '0', '0', '0', '0', '0', '0', '1', '2', '3', '0', '0', '0', '0', '0', '0', '0']
    Mazzo_giocatoreB.extend(Mazzo_giocatoreA)
    Carte_in_gioco = [ ]
    ULTIMA_PRESA = 0
    AZIONE = 0
    numero = 0
    
    #print("BENVENUTO AL SIMULATORE DI PARTITE POSSIBILI A PELA GALÈNA")
    #print("_____________________________\n- legenda:")
    #print("☺A → giocatore A")
    #print("█ → tavola")
    #print("☺B → giocatore B\n_____________________________")
    #print("- il giocatore che inizia la partita è scelto in modo casuale")
    
    #mescolo=input("- le carte nei mazzi hanno un ordine di default, vuoi mescolarle? digita s/n → ")
    mescolo = "s"

    if mescolo == "s":
        Mazzo_intero.extend(Mazzo_giocatoreA)
        Mazzo_intero.extend(Mazzo_giocatoreA)
        random.shuffle(Mazzo_intero)
        Mazzo_giocatoreA.clear()     
        for i in range(0,20):
            Mazzo_giocatoreA.extend(Mazzo_intero[i])
            salva_A.extend(Mazzo_intero[i])
        Mazzo_giocatoreB.clear()
        for i in range(20,40):
            Mazzo_giocatoreB.extend(Mazzo_intero[i])
            salva_B.extend(Mazzo_intero[i])
        ASSEGNATUTTO()
        PRINT_GAME()
    elif mescolo == "n":
        ASSEGNATUTTO()
        PRINT_GAME()

    else: print("ERRORE, CAPRONE!")


    while len(Mazzo_giocatoreB)!=0 and len(Mazzo_giocatoreB)!=0:
        try:
            if AZIONE == 0 and ULTIMA_PRESA == 0:
                ASSEGNATUTTO()
                scelte=["a", "b"]
                #dado = random.choice(scelte) # scelta iniziale
                dado = "a"
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
            #print ("\n - il gioco è finito, andate in pace - ")
            if len(Mazzo_giocatoreA)==0:
                print('\nQuella gallina del giocatore A è stata pelata',numero)
                v="B"
                lettore(salva_A,salva_B,numero) # scrittura su file
                lettura_finale(numero,v)
            elif len(Mazzo_giocatoreB)==0:
                print('\nQuella gallina del giocatore B è stata pelata', numero)
                v="A"
                lettore(salva_A,salva_B,numero)
                lettura_finale(numero,v)
        salva_A.clear()
        salva_B.clear()
        break
    
for d in range (1,2000):
    GIOCO()
    print(d,"/2000")




