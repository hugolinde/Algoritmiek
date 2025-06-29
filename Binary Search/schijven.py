'''
Schijven tellen (binary search)
Zie READ.ME voor uitleg
'''
import os

def solve(inputregels) -> int:
    schijvenAantal = 0
    invoer = iter(inputregels)

    catalogusGrootte = int(next(invoer))
    catalogus = [int(next(invoer)) for _ in range(catalogusGrootte)]

    bestellingAantal = int(next(invoer))
    bestellingen = [int(next(invoer)) for _ in range(bestellingAantal)]

    # Overzichtje printen van invoer
    print("Invoerdata:")
    print(f"- Catalogus ({catalogusGrootte}): {', '.join(map(str, catalogus))}")
    print(f"- Bestellingen ({bestellingAantal}): {', '.join(map(str, bestellingen))}")
    print("")

    for bestelling in bestellingen:
        schijvenAantal += binarySearch(bestelling, catalogus)

    return schijvenAantal

def binarySearch(bestelling, catalogus) -> int:
    left_index, right_index = 0, len(catalogus) - 1
    best_fit = -1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if catalogus[mid_index] <= bestelling:
            best_fit = catalogus[mid_index]
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return bestelling if best_fit == -1 else bestelling - best_fit

if __name__ == "__main__":
    # Zoek bestand relatief t.o.v. scriptlocatie
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bestand_pad = os.path.join(script_dir, "schijven.in")

    # 📥 Lees invoerregels in als lijst van strings
    with open(bestand_pad, encoding="utf-8") as f:
        regels = [regel.strip() for regel in f if regel.strip()]

    print("Het aantal schijven is:", solve(regels))