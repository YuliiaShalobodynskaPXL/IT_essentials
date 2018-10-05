brutoloon = float(input('geef het brutoloon'))
vakantiegeld = 0.05 * brutoloon
print('brutoloon: ', brutoloon)
if vakantiegeld >= 350:
    print('vakantiegeld: ', vakantiegeld, sep = "")
    print('bijdrage: ', 0.08 * 350)
else:
    print('vakantiegeld: ', vakantiegeld, ', bijdrage: ', 0.08 * vakantiegeld)
