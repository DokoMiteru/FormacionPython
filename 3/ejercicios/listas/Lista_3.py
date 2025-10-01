# crea dos lista con algunos elementos y combinalas en una sola. luego elimina los elementos duplicados para que la lista al final tenga valores unico.
lista_1=[1,1,2,3]
lista_2 =[3,4,5,6]
lista_3= lista_1+lista_2
 
algo =lista_3.index(3)
lista_3.pop(algo)
algo2=lista_3.index(1)
lista_3.pop(algo2)
 
print(lista_3)