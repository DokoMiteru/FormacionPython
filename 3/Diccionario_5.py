diccionario = {'c1':'valor1', 'c2':'valor2'}
#print(diccionario)
 
resultado = diccionario['c2']
#print(resultado)
 
#clientes
 
cliente = {'nombre':'Juan',
           'apellidos':'Fuentes',
           'peso': 88,
           'talla': 1.76
           }
 
consulta= (cliente['talla'])
#print(consulta)
 
#diccionario variado
dic = {'c1': 55, # entero
       'c2':[10,20,30], #lista
       'c3': {'s1':100,'s2':200} # diccionario
       }
 
#print(dic['c1'])
#print(dic['c2'][0])
#print(dic['c3']['s2'])
#agregar
dic_2= {1:'a',2:'b'}
print(dic_2)
dic_2[3]= 'c'
print(dic_2)