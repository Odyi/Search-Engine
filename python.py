def lesInnTekst(filnavn):
    try:
        with open(filnavn, 'r', encoding='utf-8') as fil:
            tekst = fil.readlines()
        return tekst
    except FileNotFoundError:
        print(f"Feil: Finner ikke filen '{filnavn}'.")
        return []
    except Exception as e:
        print(f"En feil oppstått: {e}")
        return []


In progress
