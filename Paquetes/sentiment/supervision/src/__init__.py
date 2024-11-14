# src/__init__.py

from .data_preprocessing import text_management, data_text_management
from .utils import performance

# Definimos qué se exporta cuando se hace `from src import *`
__all__ = ['text_management', 'data_text_management', 'performance']