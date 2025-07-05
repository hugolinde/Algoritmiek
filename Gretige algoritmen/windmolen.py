def plaats_windmolens(plaatsen, d):
    # Sorteer de mogelijke bouwplaatsen op afstand
    plaatsen.sort()
    
    geplaatste_molens = []
    laatste_plek = -float('inf')

    for plek in plaatsen:
        if plek - laatste_plek >= d:
            geplaatste_molens.append(plek)
            laatste_plek = plek

    return geplaatste_molens

# Voorbeeldgegevens
bouwplaatsen = [3, 5, 7, 12, 14, 18, 21, 25, 28]
min_afstand = 6  # minimaal 6 hectometer tussen molens

resultaat = plaats_windmolens(bouwplaatsen, min_afstand)
print()
print("Input: alle hectometerpaaltjes met mogelijke bouwplaatsen:", bouwplaatsen)
print("Input: minimale afstand tussen windmolens:", min_afstand, "hectometer")
print("Geplaatste windmolens op hectometerpaaltjes:", resultaat)
