from registros_ig import app
from flask  import jsonify, render_template,request,redirect
from registros_ig.models import *


@app.route("/")
def index():
    registros=select_all()
    
    return render_template("index.html", pageTitle="Registro y movimientos de Criptomonedas",data=registros)



@app.route("/purchase", methods=["GET","POST"])
def calcular():
    if request.method=="GET":
        return render_template("purchase.html", form={})
    
    else:
        if 'calcular' in request.form:
            value_to=request.form['from_q']
            value_to_q = request.form['value_to']
            value_from_qr=request.form['value_from']
            cambio=cambios(value_from_qr,value_to_q)
            valor_pu=float(value_to)*cambio
            
            list_request={
                "value_from":request.form['value_from'],
                "from_q":request.form['from_q'],
                "value_to":request.form['value_to'],
                "to_q":str(cambio),
                "value_pu":str(valor_pu)
            }
            return render_template("purchase.html",form=list_request)

        
        if 'comprar' in request.form:
            registros=select_all()
            insert(["22023-02-06",
                    "21:25",
                    request.form['value_from'],
                    request.form['from_q'],
                    request.form['value_to'],
                    request.form['to_q']
            ])
            
            
            return redirect("/")
            
        
        

@app.route("/status")
def status():
    return "aqui status"