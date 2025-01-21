""" Aca igual """

from common_imports import asdict
from .class_models import Patient
from .data_sections import sections

# Función para mostrar los datos del paciente organizados por secciones
def print_patient_data(patient: Patient):
    print('\n--------------- Datos del Paciente ---------------')
    data = asdict(patient)

    for section in sections:
        print(f"\n{section['title']}")

        if section['title'] == '--- Datos Generales ---':
            # Mostrar UUID, Edad y Entidad (si aplica)
            print(f"UUID: {patient.uuid}")
            print(f"Edad: {patient.edad} años")
        
        if 'step' in section:
            for step in section['step']:
                attribute = step['attribute']
                is_home_address = step.get('is_home_address', False)
                if is_home_address:
                    valor = patient.domicilio.get(attribute, '')
                    nombre_campo = attribute.replace('_', ' ').capitalize()
                    print(f'{nombre_campo}: {valor}')
                else:
                    # Evitar duplicar los campos 
                    if attribute in ['fecha_nacimiento', 'edad']:
                        continue
                    valor = data.get(attribute, '')
                    nombre_campo = attribute.replace('_', ' ').capitalize()

                    # No mostrar la entidad si es None
                    if attribute == 'entidad' and not patient.entidad:
                        continue  
                    print(f'{nombre_campo}: {valor}')
        
        # Mostrar datos calculados en las secciones correspondientes
        if section['title'] == '--- Datos Clínicos ---':
            print(f"IMC: {patient.imc}")

    print('--------------------------------------------------\n')