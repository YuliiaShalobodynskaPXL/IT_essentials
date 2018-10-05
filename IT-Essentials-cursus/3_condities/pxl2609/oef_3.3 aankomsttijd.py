vertrek_uur = int(input('geef vertrek uur '))
vertrek_min = int(input('geef vertrek minuten '))
duur = int(input('geef de duur van de vlugt in minuten '))

duur_uur = duur // 60
duur_min = duur % 60

aankomst_min = vertrek_min + duur_min

if aankomst_min >= 60:
    aankomst_min_final = aankomst_min - 60
    aankomst_uur_final = vertrek_uur + duur_uur + 1
else:
    aankomst_min_final = aankomst_min
    aankomst_uur_final = vertrek_uur + duur_uur

if aankomst_uur_final > 24:
    aankomst_uur_final = aankomst_uur_final - 24

print('aankomstuur = ', aankomst_uur_final, 'aankomstminuut = ', aankomst_min_final)
