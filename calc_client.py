import xmlrpc.client

# Crear un proxy para interactuar con el servidor
proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

def mostrar_menu():
    print("\nOpciones:")
    print("1. Iniciar calculadora")
    print("2. Salir")




def iniciar_calculadora():
    while True:
        # Solicitar al usuario ingresar la operación en un solo input
        user_input = input('Ingresa la operación: ')
        
        # Verificar si el usuario quiere salir
        if user_input.lower() == 'salir':
            print("Cerrando calculadora.")
            break

        # Separar los valores del input y manejar errores
        try:
            a, operation, b = user_input.split()
            a = float(a)
            b = float(b)

            # Ejecutar la operación seleccionada
            if operation == '+':
                result = proxy.add(a, b)
            elif operation == '-':
                result = proxy.subtract(a, b)
            elif operation == '*':
                result = proxy.multiply(a, b)
            elif operation == '/':
                try:
                    result = proxy.divide(a, b)
                except ZeroDivisionError:
                    result = "Error: División por cero no permitida"
            else:
                result = "Operación no válida"
        except ValueError:
            result = "Entrada inválida"
        except Exception as e:
            result = f"Ocurrió un error: {e}"

        print(result)

# Mostrar el menú principal
while True:
    mostrar_menu()
    opcion = input("\nElige una opción (1, 2, o 3): ")

    if opcion == '1':
        iniciar_calculadora()
    elif opcion == '2' or opcion.lower() == 'salir':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")
