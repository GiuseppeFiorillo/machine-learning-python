from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def main() -> None:
    # Ogni riga rappresenta un esempio
    # In questo caso abbiamo una sola caratteristica.

    study_hours = np.array(
        [
            [0.5],
            [1.5],
            [2.5],
            [3.5],
            [4.5],
            [5.5]
        ]
    )

    # Risultato osservato per ciascun esempio.
    exam_scores = np.array([45.0, 55.0, 61.0, 69.0, 77.0, 86.0])

    # Creazione del modello
    model = LinearRegression()

    # Il modello apprende la relazione tra ore e punteggio
    model.fit(study_hours, exam_scores)

    line_x = np.linspace(0.5, 6.0, 100).reshape(-1, 1)
    line_y = model.predict(line_x)

    # Predizione per un nuovo studente.
    new_student = np.array([[0.5]])
    predicted_score = model.predict(new_student)

    print(f"Coefficiente: {model.coef_[0]:.2f}")
    print(f"Intercetta: {model.intercept_:.2f}")
    print(
        "Punteggio previsto per 6 ore di studio: "
        f"{predicted_score[0]:.2f}"
    )

    plt.scatter(study_hours, exam_scores, label="Dati osservati")
    plt.plot(line_x, line_y, label="Retta appresa")

    plt.xlabel("Ore di studio")
    plt.ylabel("Punteggio")
    plt.title("Prima regressione lineare")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()