import random
rigioco="s"

while rigioco=="s": 
        forza_A=0
        forza_B=0
        print("GIOCA A SPACCABARRIERA (2 giocatori)")
        nome_A = input("Giocatore 1, digita il tuo nome: ")
        nome_B = input("Giocatore 2, digita il tuo nome: ")

        parte_A =['☺','█','█','█','█','█','█','█','█']

        parte_B = ['█','█','█','█','█','█','█','█','☺']


        occorrono_A = abs(parte_A.count('█')-9)
        occorrono_B = abs(parte_B.count('█')-9)
        occorrono = 0
        turno = 0

        def STAMPA_GIOCO():
            global parte_A
            global parte_B
            campo=[" ".join(parte_A),'☼'," ".join(parte_B)]
            print("\n------------------------------------------------------------------------------")
            print("\nRaggiungi per primo il sole spaccando le barriere!\n\n("+nome_A+","+"forza:"+str(forza_A)+")",str(" ".join(campo)) ,"("+nome_B+","+"forza:"+str(forza_B)+")")
            
        def definisci_turno():
            global turno
            if turno == nome_A:
                turno = nome_B
            elif turno == nome_B:
                turno = nome_A
            elif turno==0:
                lista=(str(nome_A),str(nome_B))
                turno = random.choice(lista)
                
        def definisci_occorrono():
            global occorrono
            global turno
            global parte_A
            global parte_B
            occorrono_A = abs(parte_A.count('█')-9)
            occorrono_B = abs(parte_B.count('█')-9)
            if turno == nome_A:
                occorrono = occorrono_A
            elif turno == nome_B:
                occorrono = occorrono_B
         
        def menu():
            while True:
                print("\nTURNO DI", turno, "- AZIONI:")
                print(" 1. Salta il turno per guadagnare 1 punto forza")
                print(" 2. Spacca una barriera (occorrono", occorrono, "punti forza)")
                print(" 3. Tira il dado")
                print(" 4. Togli un punto forza all'altro giocatore saltando il turno")
                scelta = input("Digita il numero: ")
                try:
                    if int(scelta) == 2:
                        spacca_barriera()
                    elif int(scelta)== 1:
                        salta_turno()
                    elif int(scelta) == 4:
                        togli_forza()
                    elif int(scelta) == 3:
                        tira_dado()
                except:
                    ValueError
                    continue
                else:
                    print("RITENTA, VALORE SBAGLIATO!")
                    continue


        def tira_dado():
            global turno
            global forza_A
            global forza_B
            global parte_A
            global parte_B
            while True:
                print('\nTirato il dado il turno passerà all\'avversario.\nEcco i possibili risultati:')
                print(" Se 1, guadagna 1 punto forza")
                print(" Se 2, guadagna 2 punti forza")
                print(" Se 3, guadagna 3 punti forza")
                print(" Se 4, non succede nulla")
                print(" Se 5, aggiunge una barriera al tuo percorso")
                print(" Se 6, aggiunge una barriera al percorso dell'avversario")
                print("\nA = tira il dado; B = indietro")
                scelta=input('Digita A\B: ')
                if scelta =="B":
                    menu()
                elif scelta =="A":
                    dado=random.randrange(1,6)
                    print('risultato dado:', dado)
                    if turno== nome_A:
                        if dado==1:
                            forza_A +=1
                            menu_turno()
                        elif dado==2:
                            forza_A +=2
                            menu_turno()
                        elif dado==3:
                            forza_A +=3
                            menu_turno()
                        elif dado==4:
                            menu_turno()
                        elif dado==5:
                            parte_A.insert(8,'█')
                            if " " in parte_A:
                                del parte_A[0]
                            menu_turno()
                        elif dado==6:
                            parte_B.insert(0,'█')
                            if " " in parte_B:
                                del parte_B[9]
                            menu_turno()
                            
                    elif turno== nome_B:
                        if dado==1:
                            forza_B +=1
                            menu_turno()
                        elif dado==2:
                            forza_B +=2
                            menu_turno()
                        elif dado==3:
                            forza_B +=3
                            menu_turno()
                        elif dado==4:
                            menu_turno()
                        elif dado==5:
                            parte_B.insert(0,'█')
                            if " " in parte_B:
                                del parte_B[9]
                            menu_turno()
                        elif dado==6:
                            parte_A.insert(8,'█')
                            if " " in parte_A:
                                del parte_A[0]
                            menu_turno()
                else:
                    print("ritenta")
                    continue
        def menu_turno():
            controlla_vincitore()
            definisci_turno()
            definisci_occorrono()
            STAMPA_GIOCO()
            menu()
                                
        def salta_turno():
            global forza_B
            global forza_A
            if turno == nome_A:
                forza_A += 1
                menu_turno()
            elif turno == nome_B:
                forza_B += 1
                menu_turno()
                
        def togli_forza():
            global forza_B
            global forza_A
            if turno == nome_A and forza_B !=0:
                forza_B-= 1
                menu_turno()
            elif turno == nome_B and forza_A !=0:
                forza_A -= 1
                menu_turno()
                
        def controlla_vincitore():
            global rigioco
            if parte_A.count('█')==0:
                print (nome_A, "HA VINTO LA PARTITA!")
                rigioco=input("Volete rigiocare, s\n? ")
                exit
            elif parte_B.count('█')==0:
                print (nome_B, "HA VINTO LA PARTITA!")
                rigioco=input("Volete rigiocare, n\s? ")
                exit


        def spacca_barriera():
            global parte_A
            global parte_B
            global forza_A
            global forza_B
            global occorrono
            if turno == nome_A and int(forza_A) >= int(occorrono):
                del parte_A[8]
                parte_A.insert(0, " ")
                print("Barriera spaccata!")
                menu_turno()
            elif turno == nome_B and int(forza_B) >= int(occorrono):
                del parte_B[0]
                parte_B.insert(9, " ")
                print("Barriera spaccata!")
                menu_turno()
            else:
                print("Non hai abbastanza forza!")
                menu()

        menu_turno()
        if rigioco=="n":
            break
        else:
            print("ERRORE NELL'INPUT")
            controlla_vincitore()

