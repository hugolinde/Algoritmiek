# Algoritmiek: Gretige algoritmen
Een gretig algoritme maakt bij elke stap de lokaal optimale keuze, in de hoop dat dit uiteindelijk leidt tot de globaal optimale oplossing.
Het kiest steeds wat op dat moment het beste lijkt, zonder terug te kijken of rekening te houden met toekomstige gevolgen.

Kenmerken
- Snel en eenvoudig te implementeren
- Geen backtracking of tussenopslag nodig
- Werkt alleen correct als het probleem de greedy-eigenschap heeft: een lokaal optimum leidt tot het globale optimum

## Probleem: goedkoop wijn inkopen
*Programma: wijnexpert.py*

Je wil C flessen van een specifieke champagne kopen voor oudjaarsavond. Er zijn n winkels waar je deze champagne kan kopen. 
Voor elke winkel i weten we de prijs p_i en de hoeveelheid flessen die ze op voorraad hebben c_i.
Wat is een goede gretige strategie om de kosten te minimaliseren?  
Antwoord: bezoek de winkels op volgorde van aflopende prijs. Tijdcomplexiteit O(n log n)

## Probleem: windmolens plaatsen
*Programma: windmolen.py*

Je wil langs een snelweg zo veel mogelijk windmolens bouwen, maar je kunt dat alleen doen op een beperkte set van geschikte locaties. Elke mogelijke locatie is gegeven als een hectometerpaaltje (bijvoorbeeld 3, 7, 12, ...). Verder geldt de voorwaarde dat de afstand tussen twee windmolens minimaal d hectometer is. Wat is een goede gretige strategie om een maximaal aantal windmolens te kunnen plaatsen?  
Antwoord: kies telkens de eerstvolgende plek die mogelijk is, vanaf de laatst geplaatste windmolen. Tijdcomplexiteit O(n log n)

```bash