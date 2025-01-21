""" Igual luego le pongo acá algo """

from .data_validator import sys, ValidationError

# Función para solicitar datos
def request_data(message: str, validation_function, optional=False, **kwargs):
    # Iniciar el bucle para solicitar el dato
    while True:
        # Solicitar el valor
        value = input(message).strip()

        # Identificar si el usuario ingresó un comando o no
        if value.lower() in ['back', 'exit']:
            match value.lower():
                case 'back':
                    return 'back'
                case 'exit':
                    sys.exit('Saliendo...')

        # Identificar si el valor ingresado no está vacío, si está vacío pero es opcional no hay bronca            
        if value == '':
            if optional:
                return None
            else:
                print('Por favor ingrese un valor')
                continue
        else:
            # En caso de haber ingresado un valor, validarlo y limitarlo con sus argumentos
            try:
                return validation_function(value, **kwargs)
            except ValidationError as e:
                print(f"Error: {e}")