import random

def spiel():
    auswahl = ["stein", "papier", "schere"]
    
    spieler_auswahl = input("Für ws entscheidest du dich? (stein, papier oder schere)").lower()
    
    if spieler_auswahl not in auswahl:
        print("Idiot falsche eingabe, Bitte waehle stein, papier oder schere.")