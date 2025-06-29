def aantal_stappen(n):
    if n == 0:
        return 0
    return 2 * aantal_stappen(n - 1) + 1

def hanoi(n, bron='A', hulp='B', doel='C'):
    if n == 1:
        print(f"Verplaats schijf 1 van {bron} naar {doel}")
    else:
        hanoi(n - 1, bron, doel, hulp)
        print(f"Verplaats schijf {n} van {bron} naar {doel}")
        hanoi(n - 1, hulp, bron, doel)

if __name__ == "__main__":
    print()
    n = int(input("Voer het aantal schijven in: "))
    if n < 1:
        print("Aantal schijven moet minstens 1 zijn.")
    print(f"Aantal benodigde stappen: {aantal_stappen(n)}\n")
    stappen_zien = input("Wil je ook alle stappen zelf zien? (ja/nee): ").strip().lower()
    if stappen_zien in ("ja", "j", "yes", "y"):
        print("Alle stappen:")
        hanoi(n)
    else:
        print("Stappen worden niet getoond.")
    print()
