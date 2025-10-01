#1.- INSERTAR un texto (pasar el texto original a minusculas)        done
# añadir 3 LETRAS cualquiera done                                    done
# Almacenar letras en una listas                                     done
# Cuantificar numero de apariciones de las letras                    done
 
#2 cuantificar las  PALABRAS hay en una texto >( transformalo en una lista y con una funcion averiguar el largo. ) done
#3 Decir la PRIMERA y ULTIMA LINEA DE TEXTO.                         done
#4 invertir el texto                                                 done
#5 Cuantificar numero de veces que aparece la palabra "python" en el texto done
# cuantas veces boolenos y un diccionario.
 
# Esto es un texto para python
 
texto = input("introduce un texto -> ").lower()
letras=input("introduce 3 letras -> ").lower()
lista_letra=[letras[0], letras[1], letras[2]]
lista_texto= texto.split() #tranformacion del texto en lista.
total_caracteres =len(texto)
mi_lista_reves= lista_texto
mi_lista_reves.reverse()
print(f"el número de veces que aparece la letra:\n {lista_letra[0]} ->  {texto.count(lista_letra[0])} \n {lista_letra[1]} -> {texto.count(lista_letra[1])}\n {lista_letra[0]} -> {texto.count(lista_letra[2])}")
print(f"el numero de letras que tiene el texto es : \n", total_caracteres)
print(f"la primera palabra es: {lista_texto[0]} \n la ultima palabra es: {lista_texto[-1]}")
print(f"texto al reves {mi_lista_reves}")
 
 #falta cuantas veces aparece python
 
total_apariciones= tuple(lista_texto)
print("tuplas")
print(total_apariciones.count("python"))
print("python" in total_apariciones)