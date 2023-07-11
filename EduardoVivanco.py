import numpy as np

departamentos = np.zeros(100)
asistentes = []

cantg = 0
cants = 0
cantp = 0

def disponibilidaddpto():
    print("departamentos disponibles: ")
    print("-------------------------")
    
    for depto, disponible in enumerate(departamentos):
        if disponible == 0:
            
            print(depto + 1, end="")
            
        else:
            
            print("X", end="")
            
            if(depto + 1) %10 ==0:
                
                print()
                
        print("--------------")
        
def venderdpto(rut,nombre):
    asistente = []
    
    menu= True
    
    while menu:
        numdepto = int(input("¿cual depto desea comprar?: "))
        
        if numdepto > 0 and numdepto < 4:
            print("Tipo A, 3.800 UF")
            print("Tipo B, 3.000 UF")
            print("Tipo C, 2.800 UF")
            print("Tipo D, 3.500 UF")
            print("------------------")
            
            for i in range (0, numdepto,1):
                numdepto = int(input("seleccione el tipo de dpto:"))
                
                if numdepto < 1 or numdepto > 5:
                    
                    print("depto no valido...")
                    
                elif departamentos [numdepto - 1] == 1:
                    
                    print("no esta disponible...")
                    
                else:
                    departamentos[numdepto - 1] =1
                    print(f"El depto {numdepto} ha sido vendido al comprador {nombre} , rut: {rut[:2]}.{rut[2:5]}.{rut[5:8]}-{rut[8:9]}")
                    asistente.append(nombre)
                    asistente.append(f"{rut[:2]}.{(rut[2:5])}.{(rut[5:8])}-{(rut[8:9])}")
                    asistentes.append(asistente)
                    asistentes == asistentes.sort()
                    
                    menu = False
                    
                    print("----------------------------------------------------------------------------")
                    
        else:
                    print("Ingrese entre 1 y 4....")
                    
def calcularganancia(cantp, cantg, cants):
    for TipoA in departamentos[:10]:
        if TipoA != 0:
            cantp += 1
            
    for TipoB in departamentos[:10]:
        if TipoB != 0 :
             cantg += 1
                    
    for TipoC in departamentos[:10]:
        if TipoC !=0 :
            cants += 1
            
ptotal = cantp * 3800 * 7600
gtotal =  cantg * 3000 * 6000
stotal = cants * 2800 * 5600

print("Tipo de depto       / cantidad  / total ")
print(f"TipoA - $3800   / {cantp}      / {cantp*3800*7600}")
print(f"TipoB - $3000   / {cantg}      / {cantg*3000*6000}")
print(f"TipoC - $2800   / {cants}      / {cants*2800*5600}")
print(f"Total           / {cantp+cantg+cants}    /  {ptotal+gtotal+stotal}")

def mostrarcompradores(asistentes):
    for run in asistentes:
        print(f"{run[0]} / {run[1]}")
        
        def salir():
            print("Sistema otorgado por antonia valladares")
            print("saliendo del sistema")
            
            def menu():
                
                while True:
                    print("Bienvenido(a) a Imboliaria Cajita Feliz")
                    print("---------------------------------------")
                    print("1)Comprar departamento")
                    print("2)Mostrar ubicaciones disponibles")
                    print("3)Ver listado de asistentes")
                    print("4)Mostrar ganancias totales")
                    print("5)Salir")
                    
                    opcion = int(input("Ingrese opcion: "))
                    
                    if opcion == 1:
                        
                        nombre = input("Ingrese nombre y apellido del comprador: ")
                        while True:
                            rut = input("Ingrese rut del comprador: ")
                            rut = rut.lower()
                            if len(rut) == 9:
                                if (rut [:8].isdigit()and rut[8:9].isdigit() or (rut[:8].isdigit() and rut [8:9] == "K")):
                                    venderdpto(rut,nombre)
                                    break
                                else:
                                    print("Ingrese el rut correcto")
                                    
                            elif opcion == 2:
                                    mostrarcompradores()
                                    
                            elif opcion == 3:
                                print("Asistente de compras: ")
                                mostrarcompradores(asistentes)
                                
                            elif opcion == 4:
                                calcularganancia(cantp, cantg,cants)
                                
                            elif opcion == 5:
                                salir()
                                break
                            
                            else:
                                print("Ingrese una opcion valida...")
                                
                                menu()
                                    