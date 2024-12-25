import random

class Wuerfel:
    def __init__(self, name, seiten, farbe_augen, farbe_wuerfel):
        """Initialisiert den Würfel mit den benutzerdefinierten Werten."""
        self.name = name
        self.seiten = seiten
        self.farbe_augen = farbe_augen
        self.farbe_wuerfel = farbe_wuerfel

    def werfen(self):
        """Würfelt den Würfel und gibt das Ergebnis zurück."""
        return random.choice(self.seiten)

def wuerfeln_und_anzeigen(spieler1, spieler2, wuerfel1, wuerfel2):
    """Führt die Würfelwürfe aus und gibt die Ergebnisse aus."""
    ergebnisse1 = []
    ergebnisse2 = []
    gewinne1 = 0
    gewinne2 = 0

    while gewinne1 < 3 and gewinne2 < 3:
        # Würfeln der Spieler
        wurf1 = wuerfel1.werfen()
        wurf2 = wuerfel2.werfen()

        # Ergebnisse sammeln
        ergebnisse1.append(wurf1)
        ergebnisse2.append(wurf2)

        # Anzeigen der geworfenen Werte
        print(f"{spieler1} würfelt {wuerfel1.name}: {wurf1}")
        print(f"{spieler2} würfelt {wuerfel2.name}: {wurf2}")

        # Vergleiche der Würfelergebnisse
        if wurf1 > wurf2:
            gewinne1 += 1
            print(f"{spieler1} gewinnt diese Runde!")
        elif wurf2 > wurf1:
            gewinne2 += 1
            print(f"{spieler2} gewinnt diese Runde!")
        else:
            print("Unentschieden!")

        print(f"Zwischenstand: {spieler1}: {gewinne1} | {spieler2}: {gewinne2}")
        print("-" * 40)

    if gewinne1 > gewinne2:
        print(f"{spieler1} hat gewonnen! {gewinne1} zu {gewinne2}")
    else:
        print(f"{spieler2} hat gewonnen! {gewinne2} zu {gewinne1}")
    return gewinne1, gewinne2, ergebnisse1, ergebnisse2

def neues_spiel():
    """Fragt nach, ob ein neues Spiel gestartet werden soll."""
    antwort = input("Möchtest du ein neues Spiel starten? (ja/nein): ").lower()
    return antwort == "ja"

def starte_wuerfelspiel():
    """Startet das Würfelspiel für zwei Spieler."""
    # Definieren der Würfel
    wuerfel1 = Wuerfel("Würfel 1 (Rot)", [0, 6, 6, 6, 6, 6], "gelb", "rot")
    wuerfel2 = Wuerfel("Würfel 2 (Limegrün)", [1, 1, 7, 7, 7, 7], "schwarz", "limegrün")
    wuerfel3 = Wuerfel("Würfel 3 (Blau)", [2, 2, 2, 8, 8, 8], "rosa", "blau")
    wuerfel4 = Wuerfel("Würfel 4 (Schwarz)", [3, 3, 3, 3, 9, 9], "gelb", "schwarz")
    wuerfel5 = Wuerfel("Würfel 5 (Holzfarbe)", [4, 4, 4, 4, 4, 10], "schwarz", "holzfarbe")
    wuerfel6 = Wuerfel("Würfel 6 (Braun)", [5, 5, 5, 5, 5, 5], "weiß", "braun")

    # Spieleranmeldung
    spieler1 = input("Gib den Namen des ersten Spielers ein: ")
    spieler2 = input("Gib den Namen des zweiten Spielers ein: ")

    while True:
        # Auswahl der Würfel durch die Spieler
        print("\nWürfel zur Auswahl:")
        print("1. Würfel 1 (Rot)(0)(6)(6)(6)(6)(6)")
        print("2. Würfel 2 (Limegrün)(1)(1)(7)(7)(7)(7)")
        print("3. Würfel 3 (Blau)(2)(2)(2)(8)(8)(8)")
        print("4. Würfel 4 (Schwarz)(3)(3)(3)(3)(9)(9)")
        print("5. Würfel 5 (Holzfarbe)(4)(4)(4)(4)(4)(10)")
        print("6. Würfel 6 (Braun)(5)(5)(5)(5)(5)(5)")

        wuerfel1_auswahl = int(input(f"{spieler1}, wähle deinen Würfel (1-6): "))
        wuerfel2_auswahl = int(input(f"{spieler2}, wähle deinen Würfel (1-6): "))

        # Auswahl der Würfel basierend auf der Eingabe
        wuerfel_map = {
            1: wuerfel1,
            2: wuerfel2,
            3: wuerfel3,
            4: wuerfel4,
            5: wuerfel5,
            6: wuerfel6,
        }

        wuerfel1_ausgewählt = wuerfel_map[wuerfel1_auswahl]
        wuerfel2_ausgewählt = wuerfel_map[wuerfel2_auswahl]

        # Das Würfeln und die Ausgabe
        gewinne1, gewinne2, ergebnisse1, ergebnisse2 = wuerfeln_und_anzeigen(spieler1, spieler2, wuerfel1_ausgewählt, wuerfel2_ausgewählt)

        # Frage nach einem neuen Spiel
        if not neues_spiel():
            print("Das Spiel wurde beendet.")
            break

# Start des Spiels
starte_wuerfelspiel()
