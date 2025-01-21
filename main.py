""" Este es el main """

from modules import collect_patient_data, predict_cardio, predict_diabetes, fill_word_template
# Función principal
def main():

    # Iniciar el ingreso de los datos del paciente
    choice = True
    while choice:
        # Extraer los datos del paciente
        patient = collect_patient_data()

        # Evaluar los datos
        print("\nRealizando predicciones...")
        cardio_prediction = predict_cardio(patient)
        diabetes_prediction = predict_diabetes(patient)
        
        # Mostrar el reporte médico
        press_any_key = str(input("Análisis terminado, pulse cualquier tecla para imprimir el reporte médico: "))
        print("\n")
        if press_any_key or not press_any_key:
            fill_word_template(patient, "report.docx")
        
        # Preguntarle al usuario si desea continuar
        while True:
            choice = str(input("\nSi desea ingresar a otro paciente, escriba 'continuar', en caso de que desee salir, escriba 'salir': ")).lower()
            if choice == 'continuar':
                break
            elif choice == 'salir':
                print("Saliendo...")
                choice = False
                break
            else:
                print("Entrada inválida, no puede caminar")


if __name__ == "__main__":
    main()