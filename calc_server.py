from xmlrpc.server import SimpleXMLRPCServer

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Crear el servidor en el puerto 9000
server = SimpleXMLRPCServer(('localhost', 9000))
print("Servidor escuchando en el puerto 9000...")

# Registrar las funciones en el servidor
server.register_function(add_numbers, 'add')
server.register_function(subtract_numbers, 'subtract')
server.register_function(multiply_numbers, 'multiply')
server.register_function(divide_numbers, 'divide')

# Mantener el servidor activo
server.serve_forever()
