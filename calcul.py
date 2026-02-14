# Importation des modules nécessaires
import math  # Module pour les fonctions mathématiques (log, sqrt)
import tkinter as tk  # Module pour créer des interfaces graphiques
from tkinter import simpledialog, messagebox  # Fenêtres de dialogue et messages


def calculer(nombre):
    """Calcule le logarithme et la racine carrée d'un nombre."""
    # Liste pour stocker les résultats
    resultats = []

    # Calcul du logarithme (uniquement si le nombre est strictement positif)
    if nombre > 0:
        # Logarithme en base 10 (ex: log10(100) = 2)
        resultats.append(f"Logarithme (base 10) : {math.log10(nombre):.4f}")
        # Logarithme naturel en base e (ln)
        resultats.append(f"Logarithme naturel (ln) : {math.log(nombre):.4f}")
    else:
        # Message d'erreur si le nombre est négatif ou nul
        resultats.append("Logarithme : impossible (le nombre doit être > 0)")

    # Calcul de la racine carrée (uniquement si le nombre est positif ou nul)
    if nombre >= 0:
        # Racine carrée (ex: sqrt(9) = 3)
        resultats.append(f"Racine carrée : {math.sqrt(nombre):.4f}")
    else:
        # Message d'erreur si le nombre est négatif
        resultats.append("Racine carrée : impossible (le nombre doit être >= 0)")

    # Retourne tous les résultats séparés par des sauts de ligne
    return "\n".join(resultats)


def main():
    # Création de la fenêtre principale (invisible)
    root = tk.Tk()
    root.withdraw()  # Cache la fenêtre principale

    # Affiche une fenêtre de dialogue pour demander un nombre à l'utilisateur
    nombre_str = simpledialog.askstring("Calcul", "Entrez un nombre :")

    # Si l'utilisateur a cliqué sur "Annuler", on quitte
    if nombre_str is None:
        return

    # Conversion du texte en nombre décimal
    try:
        nombre = float(nombre_str)  # Convertit la chaîne en nombre
    except ValueError:
        # Si la conversion échoue, affiche un message d'erreur
        messagebox.showerror("Erreur", f"'{nombre_str}' n'est pas un nombre valide.")
        return

    # Appelle la fonction de calcul
    resultat = calculer(nombre)

    # Affiche les résultats dans une fenêtre d'information
    messagebox.showinfo("Résultats", f"Nombre : {nombre}\n\n{resultat}")


# Point d'entrée du programme
# Ce bloc s'exécute uniquement si le fichier est lancé directement
if __name__ == "__main__":
    main()
