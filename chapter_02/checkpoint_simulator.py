"""
Per un numero di epoche scelto dall'utente, stampa la loss simulata a ogni epoca 
e il messaggio "Checkpoint salvato" ogni 5 epoche. Arresta anticipatamente quando 
la loss scende sotto una soglia scelta.
"""

def main() -> None:
    max_epochs = int(input("Numero di epoche: "))
    if max_epochs <= 0:
        print("Errore: il numero di epoche dev'essere positivo")
        return

    learning_rate = float(
        input("Tasso d'apprendimento [0-1]: ").replace(",", ".")
    )
    if not 0.0 < learning_rate < 1.0:
        print("Errore: il learning rate dev'essere maggiore di 0 e minore di 1")
        return

    target_loss = float(
        input("Loss obiettivo: ").replace(",", ".")    
    )
    if target_loss <= 0.0:
        print("Errore: la loss obiettivo dev'essere positiva").replace(",", ".")
        return

    epoch = 0
    loss = 1.0

    while epoch < max_epochs and loss > target_loss:
        epoch += 1
        loss *= 1 - learning_rate

        print(f"Epoca {epoch:03d}: loss = {loss:.6f}")     

        if epoch % 5 == 0:
            print("! Checkpoint salvato !")

    print("\n=== Fine simulazione ===")

    if loss <= target_loss:
        print(f"Obiettivo raggiunto all'epoca {epoch}.")
    else:
        print("Raggiunto il numero massimo di epoche.")
    
    print(f"Loss finale: {loss:.6f}")
        
if __name__ == "__main__":
    main()