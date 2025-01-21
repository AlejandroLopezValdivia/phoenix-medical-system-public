""" Luego le pongo pa que sirve este módulo """

from .common_imports import dataclass, Optional, field, uuid, datetime

# Clase para manejar excepciones de validación
class ValidationError(Exception):
    pass

# Clase Paciente utilizando dataclass para más papa
@dataclass
class Patient:
    # Datos Generales
    uuid: str = field(default_factory=lambda: str(uuid.uuid4()))
    nombre: str = ''
    apellido_p: str = ''
    apellido_m: str = ''
    fecha_nacimiento: datetime = None
    edad: int = 0
    sexo: str = ''
    genero: Optional[str] = None
    pais: str = ''
    entidad: Optional[str] = None 
    # Datos de Contacto
    telefono: str = ''
    correo_electronico: str = ''
    # Domicilio
    domicilio: dict = field(default_factory=dict)
    # Datos Clínicos
    estatura: int = 0
    peso: float = 0.0
    imc: float = 0.0
    cintura: int = 0
    presion_sistolica: int = 0
    presion_diastolica: int = 0
    colesterol_total: float = 0.0
    colesterol_ldl: float = 0.0
    colesterol_hdl: float = 0.0
    trigliceridos: float = 0.0
    ia: float = 0.0
    glucosa: float = 0.0
    HbA1c: float = 0.0 
    # Antecedentes
    fumador: bool = False
    alcoholico: bool = False
    activo: bool = False
    diabetes: bool = False
    hipertension: bool = False
    cardiovascular: bool = False
    cerebrovascular: bool = False
    familiares_diabetes: bool = False
    familiares_hipertension: bool = False
    familiares_cardiovascular: bool = False
    familiares_cerebrovascular: bool = False

    # Función para calcular el imc del paciente
    def calculate_bmi(self):
        try:
            self.imc = round(self.peso / ((self.estatura / 100) ** 2), 2)
        except ZeroDivisionError:
            self.imc = 0

    # Función para calcular la edad del paciente
    def calculate_age(self):
        today = datetime.today().date()
        self.edad = today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )