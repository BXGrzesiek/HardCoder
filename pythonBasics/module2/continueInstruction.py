#contiunue - pomijanie elementu i pętla leci dalej

#for a in range(0,10):
#    if a==2 or a==5:
#        continue
#    print(a)

#---------------
#for a in range(-10,10):
#    if a==0:
#        continue
#    print(100/a)

#Korzystając z continue wypisz wszystkie liczby parzyste z przedziału od 0 do 99
for i in range(0,100):
    if i % 2 == 1:
        continue
    print (i)