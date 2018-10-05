vertrek_uur = int(input('geef vertrek uur'))
vertrek_min = int(input('geef vertrek minuten'))
duur = int(input('geef de duur van de vlugt in minuten'))
vertrektijd = vertrek_uur * 60 + vertrek_min
aankomsttijd_in_min = vertrektijd + duur
