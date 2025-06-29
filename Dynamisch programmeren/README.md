# Algoritmiek: Dynamisch programmeren
Dynamisch programmeren is een algoritmische techniek waarmee je problemen oplost door ze op te splitsen in overlappende deelproblemen, waarvan je de oplossingen opslaat (memoisatie), zodat je ze niet opnieuw hoeft uit te rekenen.
Het is vooral handig bij problemen met:
- Overlappende deelproblemen (zelfde subvragen keren terug)
- Optimale substructuur (optimale oplossing is opgebouwd uit optimale deeloplossingen)

Kenmerken
- Gebruikt meestal een tabel of lijst om tussenresultaten op te slaan
- Vermijdt herhaling van werk (in tegenstelling tot pure recursie)
- Wordt vaak gebruikt bij optimalisatieproblemen

## Problemen
- Knapsack probleem
- Gewogen interval planning

```bash