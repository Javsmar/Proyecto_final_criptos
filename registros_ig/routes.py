from registros_ig import app

@app.route("/")
def index():
    return "Funciona"