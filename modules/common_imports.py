""" Módulo para realizar todas las importaciones de uña """

import pandas as pd
import numpy as np

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report

import re
import sys
import uuid
import os
import openpyxl

from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import Optional
from joblib import dump, load

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from pathlib import Path
import webbrowser