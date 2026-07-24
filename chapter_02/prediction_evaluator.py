"""
Costruiamo un programma che acquisisce un'etichetta reale binaria, una probabilità prevista e una soglia. 
Il programma valida i valori, determina la classe prevista e indica se la predizione è corretta.

Requisiti:
- L'etichetta reale deve essere 0 oppure 1.
- La probabilità deve essere compresa tra 0 e 1.
- La soglia deve essere compresa tra 0 e 1.
- La classe prevista è 1 se la probabilità è maggiore o uguale alla soglia.
- Il programma calcola anche l'errore assoluto tra etichetta e probabilità.
"""

from __future__ import annotations

def main() -> None:
    print("=== Valutatore di predizione binaria ===")
    true_label = int(input("Etichetta reale (0 o 1): "))

    if true_label not in (0, 1):
        print("Errore: l'etichetta dev'essere 0 oppure 1.")
        return

    probability = float(
        input("Probabilità prevista [0-1]: ").replace(",", ".")
    )

    if not 0.0 <= probability <= 1.0:
        print("Errore: probabilità fuori intervallo")
        return

    treshold = float(
        input("Soglia di classificazione [0-1]: ").replace(",", ".")
    )

    if not 0.0 <= treshold <= 1.0:
        print("Errore: soglia fuori intervallo")
        return

    predicted_label = 1 if probability >= treshold else 0
    is_correct = predicted_label == true_label
    absolute_error = abs(true_label - probability)

    print("\n=== Risultato ===")
    print(f"Classe prevista: {predicted_label}")
    print(f"Predizione corretta: {is_correct}")
    print(f"Errore assoluto: {absolute_error:.4f}")

if __name__ == "__main__":
    main()