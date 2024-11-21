from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Crear una nueva aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'  # Requerido por Flask-SocketIO para manejar sesiones

# Inicializar SocketIO con la app Flask
socketio = SocketIO(app)

# Definir una ruta que renderiza un archivo HTML
@app.route('/')
def home():
    return render_template('index.html')

# Manejar mensajes recibidos desde el cliente
@socketio.on('message')
def handle_message(ingrediente):
    print(f'Mensaje recibido: {ingrediente}')
    send(f'Se encontró: {ingrediente}', broadcast=True)

# Ejecutar la app con soporte para WebSockets
if __name__ == '__main__':
    socketio.run(app)