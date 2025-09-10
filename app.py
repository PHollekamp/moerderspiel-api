# app.py – Mini-API zum Testen
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Erlaube Aufrufe NUR von deiner WordPress-Domain (für später wichtig)
WP_ORIGIN = os.getenv("WP_ORIGIN", "https://deineseite.de")

@app.after_request
def add_cors(resp):
    resp.headers["Access-Control-Allow-Origin"]  = WP_ORIGIN
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    resp.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    return resp

@app.route("/api/ping")
def ping():
    return jsonify({"ok": True})

if __name__ == "__main__":
    # Lokal würde 8000 genutzt; bei Render setzt die Plattform PORT
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
