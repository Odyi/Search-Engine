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
        print(f"En feil oppstått!: {e}")
        return []

# Funksjon for å skrive ut hele teksten
def printTekst(tekst):
    if not tekst:
        print("Teksten er tom eller ikke lastet.")
        return
    for linje in tekst:
        print(linje, end='')
        funnet = True
    if not funnet:
        print(f"Fant ikke ordet '{ord}' i teksten.")

# Funksjon som sjekker om et ord finnes i teksten og returnerer True/False
def finnOrd(tekst, ord):
    for linje in tekst:
        if ord in linje:
            return True
    return False

# Funksjon som finner linjene et ord finnes på
def finnLinje(tekst, ord):
    linjer = []
    for indeks, linje in enumerate(tekst, start=1):
        if ord in linje:
            linjer.append(indeks)
    return linjer

# Funksjon som teller hvor mange ganger et ord forekommer i teksten
def tellOrd(tekst, ord):
    teller = 0
    for linje in tekst:
        teller += linje.count(ord)
    return teller

# Hovedprogram for å demonstrere funksjonaliteten
def hovedprogram():
    filnavn = input("Skriv inn navnet på tekstfilen du vil lese: ")
    tekst = lesInnTekst(filnavn)

    if not tekst:
        return
