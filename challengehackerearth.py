names1 = ['Mum', 'Wolf', 'Sherlock', 'Rain']
names2 = names1
names3 = names1[:]

names2[0] = 'Sam'
names3[1] = 'Cob'

amt = 0

for ls in (names1, names2, names3):
    if ls[0] == 'Sam':
        amt+=1
    if ls[1] == 'Cob':
        amt+= 10
print(amt)