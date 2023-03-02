print("""
        -----------------------------------

        Bienvenido a la calculadora Reactor
        
        -----------------------------------
                                             """)

comando=input("Escriba 'SUMA' para efectuar una suma: ")

if comando == "SUMA":
    numeros=int(input("Escriba los nùmeros para sumar: "))
    suma=numeros
    pregunta=input("¿Desea agregar otro nùmero? ")
    while pregunta == "SI":
      numeros=int(input("Escriba los nùmeros para sumar: "))
      suma=suma+numeros
      pregunta=input("¿Desea agregar otro nùmero? ")
      if pregunta== "NO":
        print("La suma es ",suma)
        break
else:
    print("No escribiò 'SUMA', esa operaciòn aùn no està disponible")