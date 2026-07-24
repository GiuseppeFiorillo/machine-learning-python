"""
Questo programma non addestra realmente una rete neurale, ma riproduce la struttura logica di un
training loop: epoche, aggiornamento della loss, logging periodico e arresto al raggiungimento di una soglia.
"""

from __future__ import annotations

def main() -> None:
    max_epochs = int(input("Numero massimo di epoche: "))
    if max_epochs <= 0:
        print("Il numero di epoche dev'essere positivo.")
        return

    learning_rate = float(
        input("Tasso di miglioramento [0-1]: ").replace(",", ".")
    )
    if not 0.0 < learning_rate < 1.0:
        print("Il tasso dev'essere maggiore di 0 e minore di 1.")
        return

    target_loss = float(
        input("Loss obiettivo: ").replace(",", ".")
    )
    if target_loss <= 0.0:
        print("La loss obiettivo dev'essere positiva.")
        return

    epoch = 0
    loss = 1.0

    while epoch < max_epochs and loss > target_loss:
        epoch += 1
        loss *= 1.0 - learning_rate

        if epoch == 1 or epoch % 5 == 0:
            print(f"Epoca {epoch:03d}: loss = {loss:.6f}")

    print("\n=== Fine simulazione ===")

    if loss <= target_loss:
        print(f"Obiettivo raggiunto all'epoca {epoch}.")
    else:
        print("Raggiunto il numero massimo di epoche.")
    
    print(f"Loss finale: {loss:.6f}")

if __name__ == "__main__":
    main()