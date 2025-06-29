# Algoritmiek: Recursief
Een recursief algoritme is een algoritme dat zichzelf aanroept om een kleiner deel van het probleem op te lossen. Het idee: om een groot probleem op te lossen, los ik eerst een kleiner probleem op dat er sterk op lijkt.
Een recursief algoritme bestaat meestal uit:
- Basisgeval (stopt de recursie)
- Recursieve aanroep (dezelfde functie roept zichzelf aan met kleinere invoer)

## Recursieve problemen

### Toren van Hanoi
*Programma: hanoi.py*  

De Toren van Hanoi is een klassiek puzzelprobleem dat bestaat uit:
- Drie staven (meestal A, B en C genoemd).
- N schijven van verschillende grootte, gestapeld in afnemende grootte op één van de staven (bijv. paal A).
Het doel is om de hele stapel naar een andere staaf te verplaatsen (bijv. naar paal C), waarbij je slechts één schijf tegelijk mag verplaatsen, en je mag nooit een grotere schijf op een kleinere leggen.

De kracht van de recursieve oplossing ligt in het opsplitsen van het probleem in kleinere versies van zichzelf. Hier splitsen we als volgt op:
- Verplaats de bovenste n-1 schijven van A naar B (doel tijdelijk als hulp).
- Verplaats de grootste schijf (n) van A naar C.
- Verplaats de n-1 schijven van B naar C (bron tijdelijk als hulp).  
Deze drie stappen worden telkens opnieuw toegepast op een kleinere set schijven, totdat je nog maar 1 schijf hebt: de basisconditie (want n=1 geeft altijd oplossing 1). Buiten scope van deze repo, maar vind hierbij de gesloten formule voor T(n), het wiskundig bewijs en de tijdcomplexiteit.
In dit programma worden zowel het aantal als de stappen recursief uitgerekent en getoond.

```bash