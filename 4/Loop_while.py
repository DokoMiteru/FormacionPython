monedas = 5
while monedas>0:
    print(f"tengo {monedas}")
    monedas-=1
else:
    print("no tengo mas dinero")

#Parte 2

#respuesta = 's'

#while respuesta == 's':
#    respuesta = input("¿Quieres continuar ? (S/N) ->  ")
#else:
#    print("Gracias")

#Parte 3 pass

#respuesta = 's'
#while respuesta == 's':
#    pass
#print("hola")


#Parte 3 break

nombre = input("Tu nombre -> ")

for letra in nombre:
    if letra =='r':
        break
    print(letra)


 