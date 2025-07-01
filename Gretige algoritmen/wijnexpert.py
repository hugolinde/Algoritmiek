def minimale_kosten(C, winkels):
    """
    Berekent de minimale kosten om C flessen te kopen.

    Parameters:
    - C: aantal flessen dat je wilt kopen
    - winkels: lijst van tuples (prijs_per_fles, voorraad)

    Returns:
    - totale_kosten: minimale totale prijs om C flessen te kopen
    - aankopen: lijst van (prijs, aantal gekochte flessen) per winkel
    """
    # Sorteer winkels op prijs per fles (laagste eerst)
    winkels.sort(key=lambda x: x[0])

    flessen_gekocht = 0
    totale_kosten = 0
    aankopen = []

    for prijs, voorraad in winkels:
        als_nog_nodig = C - flessen_gekocht
        te_kopen = min(voorraad, als_nog_nodig)

        totale_kosten += te_kopen * prijs
        flessen_gekocht += te_kopen
        aankopen.append((prijs, te_kopen))

        if flessen_gekocht == C:
            break

    if flessen_gekocht < C:
        raise ValueError("Niet genoeg voorraad in alle winkels om C flessen te kopen.")

    return totale_kosten, aankopen

if __name__ == "__main__":
    # Voorbeeldinvoer
    C = 10
    winkels = [
        (15, 4),  # winkel 1: €15 per fles, 4 flessen
        (12, 3),  # winkel 2: €12 per fles, 3 flessen
        (20, 10), # winkel 3: €20 per fles, 10 flessen
    ]

    print("Gewenst aantal flessen:", C)
    print("Winkelgegevens (prijs per fles, voorraad):")
    for i, (prijs, voorraad) in enumerate(winkels, 1):
        print(f"  Winkel {i}: €{prijs}, voorraad: {voorraad} flessen")

    totale_kosten, aankopen = minimale_kosten(C, winkels)
    print("\nAankoopoverzicht:")
    for prijs, aantal in aankopen:
        if aantal > 0:
            print(f"  {aantal} fles(sen) gekocht voor €{prijs} per stuk")

        print(f"\nTotale minimale kosten: €{totale_kosten}")