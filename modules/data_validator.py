""" Ete modulo e pa valida' """

from .common_imports import datetime, re, sys
from .class_models import ValidationError

# Función para validar nombre 
def validate_name(value: str) -> str:
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+", value):
        raise ValidationError('El nombre no debe contener caracteres especiales o numéricos')
    return value.title()

# Función para validar fecha y registrar diferentes formatos
def validate_date(date_str: str) -> datetime:
    format_date = [
        '%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y',
        '%d.%m.%Y', '%d %b %Y', '%d %B %Y',
        '%Y.%m.%d', '%Y/%m/%d', '%Y %b %d',
        '%Y %B %d'
    ]
    for fmt in format_date:
        try:
            date = datetime.strptime(date_str, fmt).date()
            if date > datetime.today().date():
                raise ValidationError('La fecha no puede ser futura.')
            return date
        except ValueError:
            continue
    raise ValidationError('Formato de fecha no válido.')

# Función para validar el sexo del paciente
def validate_sex(sex_str: str) -> str:
    if sex_str.upper() not in ['M', 'F']:
        raise ValidationError('Sexo debe ser M o F.')
    return sex_str.upper()

# FUnción para 'validar' el genero (solo pa que no se cientan los gays)
def validate_gender(gender_str: str) -> str:
    return gender_str.capitalize()

# Función para validar el país del paciente
def validate_country(validate_str: str) -> str:
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+", validate_str):
        raise ValidationError('El país no debe contener caracteres especiales o numéricos')
    return validate_str.title()

# Función para validar el teléfono del paciente
def validate_phone_number(phone_number_str: str) -> str:
    # Patrones para diferentes formatos de números de teléfono en México
    patterns = [
        # +52 1 55-1234-5678
        r'^\+?52\s?1\s?(\d{2,3})[-\s]?(\d{4})[-\s]?(\d{4})$',
        # +52 55-1234-5678
        r'^\+?52\s?(\d{2,3})[-\s]?(\d{4})[-\s]?(\d{4})$',
        # 1 (55) 1234-5678
        r'^1\s?\(?(\d{2,3})\)?[-\s]?(\d{4})[-\s]?(\d{4})$',
        # (55)1234-5678
        r'^\(?(\d{2,3})\)?[-\s]?(\d{4})[-\s]?(\d{4})$',
        # 55-1234-5678
        r'^(\d{2,3})[-\s]?(\d{4})[-\s]?(\d{4})$',
        # 55.1234.5678
        r'^(\d{2,3})\.(\d{4})\.(\d{4})$',
        # 55 1234 5678
        r'^(\d{2,3})\s(\d{4})\s(\d{4})$',
        # 5512345678
        r'^(\d{2,3})(\d{4})(\d{4})$'
    ]

    for pattern in patterns:
        match = re.match(pattern, phone_number_str)
        if match:
            lada, first_part, second_part = match.groups()
            formatted_phone = f"{lada}-{first_part}-{second_part}"
            return formatted_phone
        
    # Si no coincide con los patrones, intentar extraer dígitos y validar
    digits = re.sub(r'\D', '', phone_number_str)
    if len(digits) == 10:
        lada = digits[:2]
        first_part = digits[2:6]
        second_part = digits[6:]
        formatted_phone = f"{lada}-{first_part}-{second_part}"
        return formatted_phone
    elif len(digits) == 11:
        lada = digits[:3]
        first_part = digits[3:7]
        second_part = digits[7:]
        formatted_phone = f"{lada}-{first_part}-{second_part}"
        return formatted_phone
    else:
        raise ValidationError('Número de teléfono no válido. Debe tener 10 u 11 dígitos')

# Función para validar el email 
def validate_email(email_str: str) -> str:
    if not re.fullmatch(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email_str):
        raise ValidationError('Correo electrónico no válido')
    return email_str.lower()

# Función para validar datos de tipo float
def validate_float(value_str: str, min_value: float = None, max_value: float = None) -> float:
    try:
        value = float(value_str)
        if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
            raise ValidationError('Valor fuera del rango permitido')
        return value
    except ValueError:
        raise ValidationError('Debe ser un número válido')

# Función para validar datos de tipo int
def validate_int(value_str: str, min_value: int = None, max_value: int = None) -> int:
    try:
        value = int(value_str)
        if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
            raise ValidationError('Valor fuera del rango permitido')
        return value
    except ValueError:
        raise ValidationError('Debe ser un número entero válido')

# Función para validar datos de tipo bool
def validate_bool(value_str: str) -> bool:
    if value_str.lower() in ['si', 's', 'yes', 'y', '1']:
        return True
    elif value_str.lower() in ['no', 'n', '0']:
        return False
    else:
        raise ValidationError('Debe responder si o no')