def CapturarGanerales():
    nombre = input ("Ingresa tu nombre: ")
    sueldo = int(input("Ingresa tu salario"))


    if sueldo>3000:
        print("El empleado ",nombre , " debe pagar impuestos" )

    else:
        print("El empleado ",nombre ," no debe pagar impuestos")