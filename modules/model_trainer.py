""" Luego le pongo pa que es este módulo """

from .common_imports import os, train_test_split, GradientBoostingClassifier, dump
from .data_processor import load_and_process_data_cardio, load_and_process_data_diabetes

# Función para entrenar el modelo de prdicción de cardiopatía
def train_gbt_model_cardio(X, y, save_path = './data/trained_models/gbt_model_cardio.pkl'):
    train_size = 0.00001

    # Crear el directorio en caso de que no exista (por cualquier cosa)
    os.makedirs(os.path.dirname(save_path), exist_ok = True)

    # Dividir los datos en conjuntos de entrenamiento y prueba 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = train_size, random_state = 1)

    # Entrenar el modelo
    gbt = GradientBoostingClassifier(n_estimators = 200, learning_rate = 0.1, max_depth = 3, random_state = 1) 
    gbt.fit(X_train, y_train)

    # Guardar el modelo
    dump(gbt, save_path)
    print(f"Modelo guardado en {save_path}")


# Función para entrenar el modelo de predicción de diabetes
def train_gbt_model_diabetes(X, y, save_path = './data/trained_models/gbt_model_diabetes.pkl'):
    train_size = 0.00001

    # Crear el directorio en caso de que no exista (por cualquier cosa)
    os.makedirs(os.path.dirname(save_path), exist_ok = True)

    # Dividir los datos en conjuntos de entrenamiento y prueba 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = train_size, random_state = 59)

    # Entrenar el modelo
    gbt = GradientBoostingClassifier(n_estimators = 100, learning_rate = 0.01, max_depth = 3, random_state = 59) 
    gbt.fit(X_train, y_train)  

    # Guardar el modelo
    dump(gbt, save_path)


def train_models():

    # Cargar el modelo para predecir cardiopatía
    print("Cargando modelo para predecir enfermedades cardiovasculares...")

    X_cardio, y_cardio = load_and_process_data_cardio()
    train_gbt_model_cardio(X_cardio, y_cardio)

    print("Modelo cargado correctamente")

    # Cargar el modelo para predecir diabetes
    print("\nCargando modelo para predecir diabetes tipo 2...")

    X_diabetes, y_diabetes = load_and_process_data_diabetes()
    train_gbt_model_diabetes(X_diabetes, y_diabetes)

    print("Modelo cargado correctamente")
