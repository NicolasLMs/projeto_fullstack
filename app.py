from flask import Flask
from controller.usuario_controller import usuario

app = Flask(__name__)

usuario(app)

if __name__ == '__main__':
    app.run(debug=True)