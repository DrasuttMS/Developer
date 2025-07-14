import funcionSumar as FS, funcionRestar as FR, funcionMulti as FM, funcionDividir as FD, funcionFactorial as FF
continuar = True
while(continuar):
    opcion = input("Ingresa 0 para salir, 1 para sumar, 2 para restar, 3 para multiplicar, 4 para dividir, 5 para factorial -->")
    if(opcion=="0"):
        print("Gracias por usar la calculadora")
        continuar = False
    else:
            if(opcion=="5"):
                print("Ingresa el numero del que quieras el factorial")
                num = int(input("Ingresa numero --> "))
            else:
                num1 = int(input("Ingrese un numero --> "))
                num2 = int(input("Ingrese otro numero --> "))
            if(opcion=="1"):
                resultado = FS.sumar(num1,num2)
                print("La suma de ambos numeros es: ",resultado)
            elif(opcion=="2"):
                resultado = FR.restar(num1,num2)
                print("La resta de ambos numeros es: ",resultado)
            elif(opcion=="3"):
                resultado = FM.multiplicar(num1,num2)
                print("La multiplicacion de ambos numeros es: ",resultado)
            elif(opcion=="4"):
                resultado = FD.dividir(num1,num2)
                print("La division de ambos numeros, en el orden ingresado es: ",resultado)
            elif(opcion=="5"):
                resultado = FF.factorial(num)
                print("La Factorial de",num, " es",resultado)