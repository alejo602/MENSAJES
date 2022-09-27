import sqlite3


def buscarUsuario(usuario,password):
    db=sqlite3.connect("mensajes.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select * from usuarios where correo='"+usuario+"' and password= '"+password+"' and estado='1'"
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    return resultado