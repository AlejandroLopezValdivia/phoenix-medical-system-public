from tests_imports import Patient, fill_word_template, datetime

def simular():
    # Crear un paciente con todos los datos completos
    paciente = Patient(
        nombre="Juan",
        apellido_p="Pérez",
        apellido_m="González",
        fecha_nacimiento=datetime(1969, 6, 15),
        edad=55,
        sexo="Masculino",
        genero="Masculino",
        pais="México",
        entidad="CDMX",
        telefono="55-1234-1234",
        correo_electronico="juan.perez@email.com",
        domicilio={"calle": "Av. Reforma", "numero": 123, "colonia": "Centro", "cp": "06000", "ciudad": "CDMX"},
        estatura=175,
        peso=85.0,
        imc=27.8,
        cintura=95,
        presion_sistolica=145,
        presion_diastolica=95,
        colesterol_total=230,
        colesterol_ldl=150,
        colesterol_hdl=40,
        trigliceridos=190,
        ia=3.5,
        glucosa=130,
        HbA1c=7.0,
        fumador=True,
        alcoholico=False,
        activo=False,
        diabetes=True,
        hipertension=True,
        cardiovascular=True,
        cerebrovascular=False,
        familiares_diabetes=True,
        familiares_hipertension=True,
        familiares_cardiovascular=True,
        familiares_cerebrovascular=False
    )

    prediccion_cardio = 1 
    prediccion_diabetes = 1  

    fill_word_template(paciente, "reporte.docx")

simular()