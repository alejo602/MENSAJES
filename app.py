
from flask import Flask, render_template,request
import hashlib
import controlador



app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("login2.html")

@app.route("/verificarUsuario",methods=['GET', 'POST'])
def verificarUsuario():
    if request.method=='POST':
        usu = request.form["txtusuario"]
        pw = request.form["txtpass"]
        
        pw2=pw.encode()
        pw2=hashlib.sha384(pw2).hexdigest() # Metodo de encriptacion "sha384" el cual genera 96 caracteres - para tener en cuenta al momento de crear el campo en la tabla que tenga esa longitud o mas. 
       
        cuenta=len(pw2) 
        print("usuario=" + usu + " | password= " + pw)
        print("# de caracteres: ",cuenta) #solo para prueba
        print("Password Encriptado: ",pw2) #solo para prueba  
       
        respuesta=controlador.buscarUsuario(usu,pw2)
        if len(respuesta)==0:
            return "<em style='color:orange'><h1> No existe el usuario </h1>... por favor verifique los datos ingresados</em>"
        else:
            return render_template("inbox.html")   


        
        #aqui se va consultar con a bd'''
        
    return render_template("inbox.html")


@app.route("/gestionUsuarios")
def gestionUsuarios():
    return render_template("gestionUsuarios.html")        
    
