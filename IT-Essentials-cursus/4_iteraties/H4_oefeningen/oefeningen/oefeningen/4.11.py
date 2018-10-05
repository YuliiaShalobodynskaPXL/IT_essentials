personeelnummer = int(input("geef personeelnummer "))

m_ouder34_of_loon_meer1800 = 0
v_jonger25 = 0

while personeelnummer != 0:
    geslacht = int(input("geef geslacht(0=vrouw, 1= man)"))
    leeftijd = int(input("geef leeftijd"))
    brutoloon = int(input("geef brutoloon"))
    if geslacht == 1:
        if leeftijd > 34 or brutoloon >= 1800:
            m_ouder34_of_loon_meer1800 += 1
    elif geslacht == 0:
        if leeftijd < 25:
            v_jonger25 += 1
    print()
    personeelnummer = int(input("geef personeelnummer "))

print()
print("Het aantal mannen die .... is ", m_ouder34_of_loon_meer1800)
print("Het aantal vrouwen die jonger dan 25 zijn is ", v_jonger25)


