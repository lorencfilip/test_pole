zbozi = ["CPU", "GPU", "RAM", "Hard disk", "Mother board"]
kosik = []

while True:
    for x in range(len(zbozi)):
        print(f"Zboží s číslem {x + 1}: {zbozi[x]}")
    
    def vypis_pole(prvek):
        for x in range(len(prvek)):
            print(f"Zboží s číslem {x + 1}: {prvek[x]}")

    prvek_minus = input("Co si chcete koupit ? ")
    zbozi.remove(prvek_minus)

    kosik.append(prvek_minus)


    print("Stav vašeho košíku")
    print(kosik)

    print("Co dalšího si chcete koupit ? ")

    if len(kosik) == 5:
        break