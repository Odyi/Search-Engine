# Funksjon for å lese inn en tekstfil
def lesInnTekst(filnavn):
    try:
        with open(filnavn, 'r', encoding='utf-8') as fil:
            tekst = fil.readlines()
        return tekst
    except FileNotFoundError:
        print(f"Feil: Finner ikke filen, Womp womp '{filnavn}'.")
        return []
    except Exception as e:
        print(f"En feil oppstod!: {e}")
        return []

# Funksjon for å skrive ut hele teksten
def printTekst(tekst):
    if not tekst:
        print("Teksten er tom eller ikke lastet.")
        return
    for linje in tekst:
        print(linje, end='')

# Funksjon som sjekker om et ord finnes i teksten og returnerer True/False
def finnOrd(tekst, ord):
    for linje in tekst:
        if ord in linje:
            return True
    return False

# Funksjon som finner linjene et ord er på
def finnLinje(tekst, ord):
    linjer = []
    for indeks, linje in enumerate(tekst, start=1):
        if ord in linje:
            linjer.append(indeks)
    return linjer

# Funksjon som teller hvor mange ganger et ord gjentar seg i teksten
def tellOrd(tekst, ord):
    teller = 0
    for linje in tekst:
        teller += linje.count(ord)
    return teller

# Funksjon for å sjekke lengden på et ord
def ordLengde(ord):
    return len(ord)

# Hovedprogram 
def hovedprogram():
    filnavn = input("Skriv inn navnet på tekstfilen du vil lese: ")
    tekst = lesInnTekst(filnavn)

    if not tekst:
        return

    while True:
        print("\nMeny:")
        print("1. Vis hele teksten")
        print("2. Søk etter et ord og vis linjer")
        print("3. Finn ut om et ord finnes i teksten")
        print("4. Tell antall av samme ord")
        print("5. Sjekk lengden av et ord")  #ord lengde test
        print("6. Avslutt")

        valg = input("Velg et alternativ (1-6): ")

        if valg == "1":
            printTekst(tekst)
        elif valg == "2":
            ord = input("Skriv inn ordet du vil søke etter: ")
            linjer = finnLinje(tekst, ord)
            if linjer:
                print(f"Ordet '{ord}' finnes på linje(r): {', '.join(map(str, linjer))}.")
            else:
                print(f"Ordet '{ord}' ble ikke funnet.")
        elif valg == "3":
            ord = input("Skriv inn ordet du vil sjekke: ")
            finnes = finnOrd(tekst, ord)
            if finnes:
                print(f"Ordet '{ord}' finnes i teksten!")
            else:
                print(f"Ordet '{ord}' finnes ikke i teksten.")
        elif valg == "4":
            ord = input("Skriv inn ordet du vil telle: ")
            antall = tellOrd(tekst, ord)
            print(f"Ordet '{ord}' dukker opp {antall} gang(er) i teksten.")
        elif valg == "5":  # test legnde
            ord = input("Skriv inn ordet du vil sjekke lengden på: ")
            lengde = ordLengde(ord)
            print(f"Lengden på ordet '{ord}' er {lengde} tegn.")
        elif valg == "6":
            print("Avslutter programmet, Ha en fin dag :)")
            break
        else:
            print("Ugyldig valg, prøv igjen.")

# Kjør hovedprogrammet
if __name__ == "__main__":
    hovedprogram()
