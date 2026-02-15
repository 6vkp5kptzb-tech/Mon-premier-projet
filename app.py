from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), "utilisateurs.db")


def init_db():
    """Initialise la base de données SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            date_naissance TEXT NOT NULL,
            departement TEXT NOT NULL,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["GET", "POST"])
def formulaire():
    message = None
    if request.method == "POST":
        nom = request.form.get("nom", "").strip()
        prenom = request.form.get("prenom", "").strip()
        date_naissance = request.form.get("date_naissance", "").strip()
        departement = request.form.get("departement", "").strip()

        if not all([nom, prenom, date_naissance, departement]):
            message = "Tous les champs sont obligatoires."
        else:
            conn = get_db()
            conn.execute(
                "INSERT INTO utilisateurs (nom, prenom, date_naissance, departement) VALUES (?, ?, ?, ?)",
                (nom, prenom, date_naissance, departement),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("liste"))

    return render_template("formulaire.html", message=message)


@app.route("/liste")
def liste():
    conn = get_db()
    utilisateurs = conn.execute(
        "SELECT * FROM utilisateurs ORDER BY date_creation DESC"
    ).fetchall()
    conn.close()
    return render_template("liste.html", utilisateurs=utilisateurs)


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
