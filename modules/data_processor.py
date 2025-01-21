""" Acá también """

from .common_imports import pd

# Función para limpiar y procesar el dataset de cardio
def load_and_process_data_cardio():
    
    # Cargar el archivo CSV
    cardio_data = pd.read_csv('data/datasets/Cardio_Data.csv')

    # Limpiar la base de datos
    cardio_data = cardio_data.dropna()

    # Calcular el BMI
    cardio_data['height'] = cardio_data['height'] / 100  # Convertir altura a metros
    cardio_data['bmi'] = cardio_data['weight'] / (cardio_data['height'] ** 2)
    
    # Separar las variables dependientes e independientes
    labels = ['age', 'ap_hi', 'ap_lo', 'bmi']
    X = cardio_data[labels]
    y = cardio_data.target
    
    return X, y

# Función para limpiar y procesar el dataset de diabetes
def load_and_process_data_diabetes():

    # Cargar el archivo xlsx
    diabetes_data = pd.read_excel('data/datasets/working data.xlsx')

    # Limpiar la base de datos
    diabetes_data = diabetes_data[diabetes_data['type'] == 'Type 2']
    diabetes_data = diabetes_data.dropna()
    
    # Separar las variables dependientes e independientes
    labels = ['HbA1c_level', 'blood_glucose_level']
    X = diabetes_data[labels]
    y = diabetes_data.diabetes

    return X, y