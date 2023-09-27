# Importa a classe Flask do módulo flask
from flask import Flask

# Cria uma instância da classe Flask e atribui a variável 'app'
app = Flask(__name__)


# Define uma rota na raiz ('/') da aplicação
@app.route('/')
# Define uma função chamada 'hello_world' que será executada quando a rota for acessada
def hello_world():
    # Retorna uma string como resposta para a rota
    return 'Hello World! Welcome to Python'


# Verifica se este arquivo está sendo executado diretamente (não importado como um módulo)
if __name__ == '__main__':
    # Inicia o servidor da aplicação Flask
    app.run()
# Importa a classe Flask do módulo flask
from flask import Flask

# Cria uma instância da classe Flask e atribui a variável 'app'
app = Flask(__name__)


# Define uma rota na raiz ('/') da aplicação
@app.route('/')
# Define uma função chamada 'hello_world' que será executada quando a rota for acessada
def hello_world():
    # Retorna uma string como resposta para a rota
    return 'Hello World! Welcome to Python'


# erifica se este arquivo está sendo executado diretamente (não importado como um módulo)
if __name__ == '__main__':
    # Inicia o servidor da aplicação Flask
    app.run()
