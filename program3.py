from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/mojastrona')
def mojastrona():
    return "To jest moja strona!"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Nieznajomy')
    return f"Witaj, {name}!"

if __name__ == '__main__':
    app.run()
