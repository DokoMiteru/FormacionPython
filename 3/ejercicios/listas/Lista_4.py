#crea una lista con 4 numero e intercambia el primero por el ultimo y el ultimo por el primero
lista=[1,2,3,4,5]
primer= lista[0]
ultimo=lista[-1]
lista[0]=ultimo
lista[len(lista)-1]= primer
 
print(lista)