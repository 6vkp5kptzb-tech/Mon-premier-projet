import math
import tkinter as tk
from tkinter import simpledialog, messagebox


def calculer(nombre):
    """Calcule le logarithme et la racine carrée d'un nombre."""
    resultats = []
    if nombre > 0:
        resultats.append(f"Logarithme (base 10) : {math.log10(nombre):.4f}")
        resultats.append(f"Logarithme naturel (ln) : {math.log(nombre):.4f}")
    else:
        resultats.append("Logarithme : impossible (le nombre doit être > 0)")

    if nombre >= 0:
        resultats.append(f"Racine carrée : {math.sqrt(nombre):.4f}")
    else:
        resultats.append("Racine carrée : impossible (le nombre doit être >= 0)")

    return "\n".join(resultats)


def main():
    root = tk.Tk()
    root.withdraw()

    nombre_str = simpledialog.askstring("Calcul", "Entrez un nombre :")
    if nombre_str is None:
        return

    try:
        nombre = float(nombre_str)
    except ValueError:
        messagebox.showerror("Erreur", f"'{nombre_str}' n'est pas un nombre valide.")
        return

    resultat = calculer(nombre)
    messagebox.showinfo("Résultats", f"Nombre : {nombre}\n\n{resultat}")


if __name__ == "__main__":
    main()
