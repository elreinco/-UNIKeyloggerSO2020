from flask import Flask
from flask import render_template
import win32console
import win32gui

#ventana=win32console.GetConsoleWindow()
#win32gui.ShowWindow(ventana,0)


app= Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0')