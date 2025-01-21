""" Lo mismo """

from .data_validator import validate_date, validate_bool, validate_country, validate_email, validate_gender, validate_float, validate_int, validate_name, validate_phone_number, validate_sex, ValidationError, re

# Definición de las secciones y step
sections = [
    {
        # Sección de datos generales del paciente
        'title': '--- Datos Generales ---',
        'step': [
            {'message': 'Nombre(s): ', 'attribute': 'nombre', 'validation': validate_name},
            {'message': 'Apellido Paterno: ', 'attribute': 'apellido_p', 'validation': validate_name},
            {'message': 'Apellido Materno: ', 'attribute': 'apellido_m', 'validation': validate_name},
            {'message': 'Fecha de Nacimiento (DD/MM/YYYY): ', 'attribute': 'fecha_nacimiento', 'validation': validate_date},
            {'message': 'Sexo (M/F): ', 'attribute': 'sexo', 'validation': validate_sex},
            {'message': 'Género: ', 'attribute': 'genero', 'validation': validate_gender},
            {'message': 'País de Nacimiento: ', 'attribute': 'pais', 'validation': validate_country},
            # Preguntar por entidad si el país es México
            {'message': 'Entidad de Nacimiento: ', 'attribute': 'entidad', 'validation': validate_country, 'condition': lambda paciente: paciente.pais.lower() in ['méxico', 'mexico']},
        ]
    },
    {
        # Sección de datos de contacto del paciente
        'title': '--- Datos de Contacto ---',
        'step': [
            {'message': 'Teléfono: ', 'attribute': 'telefono', 'validation': validate_phone_number},
            {'message': 'Correo Electrónico: ', 'attribute': 'correo_electronico', 'validation': validate_email},
        ]
    },
    {
        # Sección del domicilio del paciente
        'title': '--- Domicilio ---',
        'step': [
            {'message': 'Calle: ', 'attribute': 'calle', 'validation': validate_name, 'is_home_address': True},
            {'message': 'Número Exterior: ', 'attribute': 'numero_exterior', 'validation': lambda x: x if x.isdigit() else (_ for _ in ()).throw(ValidationError('Debe ser un número.')), 'is_home_address': True},
            {'message': 'Número Interior (optional): ', 'attribute': 'numero_interior', 'validation': lambda x: x if x == '' or x.isdigit() else (_ for _ in ()).throw(ValidationError('Debe ser un número o dejar en blanco.')), 'is_home_address': True, 'optional': True},
            {'message': 'Colonia/Barrio: ', 'attribute': 'colonia', 'validation': validate_name, 'is_home_address': True},
            {'message': 'Ciudad: ', 'attribute': 'ciudad', 'validation': validate_name, 'is_home_address': True},
            {'message': 'Estado/Provincia: ', 'attribute': 'estado', 'validation': validate_name, 'is_home_address': True},
            {'message': 'Código Postal: ', 'attribute': 'codigo_postal', 'validation': lambda x: x if re.fullmatch(r'\d{5}', x) else (_ for _ in ()).throw(ValidationError('Debe ser un código postal válido de 5 dígitos.')), 'is_home_address': True},
            {'message': 'País: ', 'attribute': 'pais', 'validation': validate_name, 'is_home_address': True},
        ]
    },
    {
        # Sección de los datos clínicos del paciente
        'title': '--- Datos Clínicos ---',
        'step': [
            {'message': 'Estatura (cm): ', 'attribute': 'estatura', 'validation': validate_int, 'kwargs': {'min_value': 50, 'max_value': 300}},
            {'message': 'Peso (kg): ', 'attribute': 'peso', 'validation': validate_float, 'kwargs': {'min_value': 20.0, 'max_value': 350.0}},
            {'message': 'Circunferencia de cintura (cm): ', 'attribute': 'cintura', 'validation': validate_int, 'kwargs': {'min_value': 40, 'max_value': 200}},
            {'message': 'Presión Sistólica (mm Hg): ', 'attribute': 'presion_sistolica', 'validation': validate_int, 'kwargs': {'min_value': 50, 'max_value': 250}},
            {'message': 'Presión Diastólica (mm Hg): ', 'attribute': 'presion_diastolica', 'validation': validate_int, 'kwargs': {'min_value': 30, 'max_value': 150}},
            {'message': 'Colesterol Total (mg/dL): ', 'attribute': 'colesterol_total', 'validation': validate_float, 'kwargs': {'min_value': 30.0, 'max_value': 1100.0}},
            {'message': 'Colesterol LDL (mg/dL): ', 'attribute': 'colesterol_ldl', 'validation': validate_float, 'kwargs': {'min_value': 30.0, 'max_value': 1000.0}},
            {'message': 'Colesterol HDL (mg/dL): ', 'attribute': 'colesterol_hdl', 'validation': validate_float, 'kwargs': {'min_value': 10.0, 'max_value': 200.0}},
            {'message': 'Triglicéridos (mg/dL): ', 'attribute': 'trigliceridos', 'validation': validate_float, 'kwargs': {'min_value': 30.0, 'max_value': 1000.0}},
            {'message': 'Índice Aterogénico: ', 'attribute': 'ia', 'validation': validate_float, 'kwargs': {'min_value': 1.0, 'max_value': 10.0}},
            {'message': 'Glucosa en ayunas (mg/dL): ', 'attribute': 'glucosa', 'validation': validate_float, 'kwargs': {'min_value': 40.0, 'max_value': 600.0}},
            {'message': 'Hemoglobina Glicosilada (%): ', 'attribute': 'HbA1c', 'validation': validate_float, 'kwargs': {'min_value': 3.5, 'max_value': 20.0}},
        ]
    },
    {
        # Sección de factores de riesgo y antecedentes del paciente
        'title': '--- Antecedentes ---',
        'step': [
            {'message': '¿Es fumador? (si/no): ', 'attribute': 'fumador', 'validation': validate_bool},
            {'message': '¿Consume alcohol? (si/no): ', 'attribute': 'alcoholico', 'validation': validate_bool},
            {'message': '¿Es físicamente activo? (si/no): ', 'attribute': 'activo', 'validation': validate_bool},
            {'message': '¿Es diabético? (si/no): ', 'attribute': 'diabetes', 'validation': validate_bool},
            {'message': '¿Tiene hipertensión? (si/no): ', 'attribute': 'hipertension', 'validation': validate_bool},
            {'message': '¿Tiene enfermedad cardiovascular? (si/no): ', 'attribute': 'cardiovascular', 'validation': validate_bool},
            {'message': '¿Tiene enfermedad cerebrovascular? (si/no): ', 'attribute': 'cerebrovascular', 'validation': validate_bool},
            {'message': '¿Tiene familiares con diabetes? (si/no): ', 'attribute': 'familiares_diabetes', 'validation': validate_bool},
            {'message': '¿Tiene familiares con hipertensión? (si/no): ', 'attribute': 'familiares_hipertension', 'validation': validate_bool},
            {'message': '¿Tiene familiares con enfermedades cardiovasculares? (si/no): ', 'attribute': 'familiares_cardiovascular', 'validation': validate_bool},
            {'message': '¿Tiene familiares con enfermedades cerebrovasculares? (si/no): ', 'attribute': 'familiares_cerebrovascular', 'validation': validate_bool},
        ]
    }
]