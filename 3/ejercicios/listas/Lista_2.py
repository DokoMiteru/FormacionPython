# dada una lista de palabras , busca la posicion  de una palabra especifica y luego reemplazala por otra.
 
lista= ["algo","patata", "diez cuatro"]
palabra_antigua = lista.index("patata")
palabra_nueva= "pasa"
lista[palabra_antigua]= palabra_nueva
 
print(lista)