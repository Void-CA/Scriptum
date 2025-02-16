from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Cargar los datos del CSV al iniciar el servidor
df = pd.read_csv("../data/mockup.csv")

@app.route("/")
def home():
    return render_template("index.html")  # Carga la página web

@app.route("/buscar", methods=["GET"])
def buscar():
    apellido = request.args.get("apellido", "").strip().lower()
    
    if not apellido:
        return jsonify({"error": "Debes ingresar un apellido"}), 400

    # Realizar búsqueda parcial ignorando mayúsculas/minúsculas
    resultados = df[df["Usuario"].str.lower().str.contains(apellido, na=False)]

    if resultados.empty:
        return jsonify({"mensaje": "No se encontraron coincidencias"})

    return jsonify(resultados.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
