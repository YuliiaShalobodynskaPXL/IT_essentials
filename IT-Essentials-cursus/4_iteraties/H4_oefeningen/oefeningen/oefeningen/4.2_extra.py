#**Oefening 4.2**

#Via het toetsenbord wordt de naam van een student en zijn behaald percentage
#ingegeven. Doe een invoercontrole op het behaald percentage (enkel 0-100 is
#toegelaten). Telkens een verkeerde invoer gebeurt, dient er op het scherm een
#foutboodschap te verschijnen. Ofwel "Fout! het getal moet minstens 0 zijn" ofwel "Fout!
#het getal mag maximum 100 zijn".
#Bepaal vervolgens de behaalde graad en druk naam en graad af.

#  60<70%	voldoende
#	 70<80%	onderscheiding
#	80<85%	grote onderscheiding
#	≥ 85%	grootste onderscheiding

#*Uitbreiding:* Het programma moet herhaald kunnen worden voor meerdere
#studenten.  Wanneer als naam “xx” of “XX” wordt ingevoerd, eindigt het programma.

naam = str(input("de naam van een student: "))

while naam != str("xx") and naam != str("XX"):
    percentage = int(input("zijn behaald percentage: "))
    if percentage < 0:
        print("Fout! het getal moet minstens 0 zijn")
    elif percentage > 100:
        print("Fout! het getal mag maximum 100 zijn")
    elif percentage < 60:
        print(naam, "<60%	onvoldoende" )
    elif percentage < 70:
        print(naam, "60<70%	 voldoende" )
    elif percentage < 80:
        print(naam, "70<80%	 onderscheiding")
    elif percentage < 85:
        print(naam, "80<85%	grote onderscheiding")
    else:
        print(naam, "≥ 85%	grootste onderscheiding")

    naam = str(input("de naam van een student: "))
