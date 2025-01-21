""" Acordarme de explicar para que sirve este módulo y mejorarlo para regresar entre secciones """

from .class_models import Patient
from .data_sections import sections
from .data_input import request_data

# Función para recolectar datos del paciente
def collect_patient_data() -> Patient:
    patient = Patient()

    # Título y message de ayuda
    print('\nIngrese "back" para regresar al paso anterior o "exit" para salir')
    print('\n--------------- Registro de Paciente ---------------')

    # Imprimir por secciones y guardar por secciones
    for section in sections:
        # Imprimir el título de la sección
        print(f"\n{section['title']}")

        if 'step' in section:
            step = section['step']
            index = 0

            # Abrir el bucle de la sección 
            while index < len(step):
                # Definir el message, attribute, validación, argumentos, y demás para cada paso dentro de la sección
                current_step = step[index]
                message = current_step['message']
                attribute = current_step['attribute']
                validation_function = current_step['validation']
                kwargs = current_step.get('kwargs', {})
                is_home_address = current_step.get('is_home_address', False)
                optional = current_step.get('optional', False)
                condition = current_step.get('condition', None)

                # Verificar si hay una condición para este paso
                if condition and not condition(patient):
                    index += 1
                    continue
                
                # Solicitar la entrada el usuario
                result = request_data(message, validation_function, optional=optional, **kwargs)


                # Retroceder step dentro de la sección
                if result == 'back':
                    if index > 0:
                        index -= 1
                        print('Retrocediendo al paso anterior...')
                    else:
                        print('Ya estás en el primer paso de esta sección pa, no puedes retroceder más')

                # Continuar y setear la respuesta
                else:
                    if is_home_address:
                        if not patient.domicilio:
                            patient.domicilio = {}
                        patient.domicilio[attribute] = result
                    else:
                        setattr(patient, attribute, result)

                    # Realizar cálculos adicionales 
                    if attribute == 'fecha_nacimiento':
                        patient.calculate_age()
                    elif attribute == 'peso' or attribute == 'estatura':
                        patient.calculate_bmi()

                    index += 1

    return patient