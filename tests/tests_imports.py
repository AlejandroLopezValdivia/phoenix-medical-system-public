import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.class_models import Patient
from modules.report_generator import fill_word_template
from modules.common_imports import datetime