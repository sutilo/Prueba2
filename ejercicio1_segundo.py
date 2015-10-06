__author__ = 'manuel'

import pdb

palabras =["abc","xd","crm","zl","xb"]

lista_x=[]
lista_s=[]

for elemento in palabras:
    pdb.set_trace()
    if elemento[0]=="x":
        lista_x.append(elemento)
    else:
        lista_s.append(elemento)



lista_final = sorted(lista_x) + sorted(lista_s)


print lista_final


