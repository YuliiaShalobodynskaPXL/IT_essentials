sterren = int(input("geef aantan sterren(1-5): "))
code = str(input("geef code(O = enkel ontbijt, H - half-pension, V - vol pension, A - all-inclisive): "))
overnachten = int(input("geef aantal overnachten: "))
seizoen =  str(input("geef seizoen(H-hoogseizoen, L - laagseizoen, T - tussenseizoen): "))

if sterren == 1:
    prijs = overnachten * 30
elif sterren < 4:
    prijs = overnachten * 40
else:
    prijs = overnachten * 55

if code == "O":
    prijs = prijs * 1.2
elif code == "H":
    prijs = prijs * 1.5
elif code == "V":
    prijs = prijs * 1.6
else:
    prijs = prijs * 1.6 + 80 * overnachten

if seizoen == "L":
    if code == "O" or code == "H" :
        prijs = prijs * 0.9

print("De prijs voor 1 persoon is: ", prijs)

