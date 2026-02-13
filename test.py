import sys
from datetime import datetime


def main():
    """Point d'entrée principal du programme."""
    print("Prêt pour Claude Code !")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Date et heure: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("un nouvel essai de MAJ")
    print(f"Bonjour, nous sommes le : {datetime.now().strftime('%d/%m/%Y')}")

if __name__ == "__main__":
    main()
