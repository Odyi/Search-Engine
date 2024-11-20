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
