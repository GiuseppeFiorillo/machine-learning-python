from __future__ import annotations

import platform
import sys

import matplotlib
import numpy as np
import pandas as pd
import sklearn

def main() -> None:
    print("=== Informazioni di sistema ===")
    print(f"Sistema operativo: {platform.system()}")
    print(f"Versione sistema: {platform.release()}")
    print(f"Architettura: {platform.machine()}")

    print("\n=== Informazioni Python ===")
    print(f"Versione Python: {sys.version}")
    print(f"Interprete: {sys.executable}")
    
    print("\n=== Librerie principali ===")
    print(f"NumPy: {np.__version__}")
    print(f"pandas: {pd.__version__}")
    print(f"Matplotlib: {matplotlib.__version__}")
    print(f"scikit-learn: {sklearn.__version__}")
    print("\nConfigurazione completata correttamente.")

if __name__ == "__main__":
    main()