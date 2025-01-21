""" Luego le pongo pa que sirve este módulo """

from .common_imports import asdict, pd, load

# Función para predecir problemas cardiovasculares
def predict_cardio(paciente):

    # Convertir los datos del paciente a un diccionario
    patient_data = asdict(paciente)

    # Mapear atributos del paciente a los nombres esperados por el modelo
    input_data = {
        'age': patient_data['edad'],  # Mapear edad
        'ap_hi': patient_data['presion_sistolica'],  # Mapear presión sistólica
        'ap_lo': patient_data['presion_diastolica'],  # Mapear presión diastólica
        'bmi': patient_data['imc'],  # Mapear IMC
    }

    # Crear un df con una fila
    df = pd.DataFrame([input_data])

    # Cargar el modelo y hacer la predicción
    gbt_cardio = load('./data/trained_models/gbt_model_cardio.pkl')
    prediction = gbt_cardio.predict(df)

    return prediction[0]  # Retornar el resultado de la predicción

def predict_diabetes(paciente):

    # Convertir los datos del paciente a un diccionario
    patient_data = asdict(paciente)

    # Mapear atributos del paciente a los nombres esperados por el modelo
    input_data = {
        'HbA1c_level': patient_data['HbA1c'],  # Mapear hemoglobina glucosilada
        'blood_glucose_level': patient_data['glucosa'],  # Mapear glucosa en sangre
    }

    # Crear un df con una fila
    df = pd.DataFrame([input_data])

    # Cargar el modelo y hacer la predicción
    gbt_cardio = load('./data/trained_models/gbt_model_diabetes.pkl')
    prediction = gbt_cardio.predict(df)

    return prediction[0]  # Retornar el resultado de la predicción
