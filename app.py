import sqlite3
import os
from flask import Flask, render_template

app = Flask(__name__)

DATABASE = "database/restaurantedb.db"

# conexión a la BD
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# ruta principal
@app.route('/')
def index():
    conn = get_db_connection()

    # restaurante
    restaurante = conn.execute(
        "SELECT * FROM restaurante LIMIT 1"
    ).fetchone()

    # menú por fecha
    fecha = '2026-03-22'
    menu = conn.execute(
        "SELECT * FROM menu_almuerzo WHERE fecha = ?", 
        (fecha,)
    ).fetchall()

    conn.close()

    return render_template(
        "index.html", 
        restaurante=restaurante, 
        menu=menu
    )

if __name__ == '__main__':
    #app.run(debug=True)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)