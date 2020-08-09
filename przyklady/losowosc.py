import random

lista = ['piosenka1', 'piosenka2', 'piosenka3']

losowy_element = random.choice(lista)
print(losowy_element)
for i in range(2):
    losowy_element = random.choice(lista)
    print(losowy_element)

losowa_lista = random.sample(lista, 2)
print(losowa_lista)
