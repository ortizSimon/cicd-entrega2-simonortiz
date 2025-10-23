#!/usr/bin/env python3
"""
Script para ejecutar la aplicación Flask
"""

import sys
import os

# Agregar el directorio actual al path de Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar como módulo para que funcionen las importaciones relativas
from app import app

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
