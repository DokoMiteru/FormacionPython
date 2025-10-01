nombre = input("Dime tu nombre -> ")
ventas =float(input("Dime el numero de ventas -> "))
 
print(f"{nombre} El número de comisión según tus {ventas} son  {round(ventas*13/100,2)}")