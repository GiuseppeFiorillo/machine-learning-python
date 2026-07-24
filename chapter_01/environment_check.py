from __future__ import annotations

import platform
import sys

import matplotlib
import numpy as np
import pandas as pd
import sklearn
import pip

import os
import platform

def main() -> None:
    print("=== Informazioni di sistema ===")
    print(f"Sistema operativo: {platform.system()}")
    print(f"Versione sistema: {platform.release()}")
    print(f"Architettura: {platform.machine()}")

    print("\n=== Informazioni processore ===")
    print(f"Nome processore: {platform.processor()}")
    print(f"Numero di core logici: {os.cpu_count()}")

    print("\n=== Informazioni Python ===")
    print(f"Versione Python: {sys.version}")
    print(f"Interprete: {sys.executable}")
    print(f"Cartella corrente: {os.getcwd()}")
    
    print("\n=== Librerie principali ===")
    print(f"NumPy: {np.__version__}")
    print(f"pandas: {pd.__version__}")
    print(f"Matplotlib: {matplotlib.__version__}")
    print(f"scikit-learn: {sklearn.__version__}")
    print(f"pip: {pip.__version__}")
    print("\nConfigurazione completata correttamente.")
if __name__ == "__main__":
    main()