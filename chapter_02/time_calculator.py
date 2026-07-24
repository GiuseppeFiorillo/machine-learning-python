"""
Chiedi numero di epoche e secondi medi per epoca. Stima il tempo totale e stampalo in ore, minuti e secondi.
"""

def main() -> None:
    num_epochs = int(input("Numero di epoche: "))
    if num_epochs <= 0:
        print("Errore: il numero di epoche dev'essere positivo")
        return
    
    avg_seconds = float(input("Numero di secondi medi per epoca: "))
    
    epoch = 0
    total_seconds = num_epochs * avg_seconds

    hours = int(total_seconds // 3600)
    remaining = total_seconds % 3600
    minutes = int(remaining // 60)
    seconds = remaining % 60

    print("=== Tempo calcolato ===")
    print(f"{hours} ore, {minutes} minuti, {seconds:.2f} secondi")

if __name__ == "__main__":
    main()