from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1>Home page</h1>
    <a href="/random_fact">¡Ver un dato aleatorio!</a>
    '''

@app.route("/random_fact")
def random_fact():
    facts = [
        "Los pulpos tienen tres corazones.",
        "La miel nunca se echa a perder.",
        "Un día en Venus dura más que un año en Venus."
    ]
    fact = random.choice(facts)
    return f"<h1>{fact}</h1>"

@app.route("/secret")
def secret():
    resultado = random.choice(["Cara", "Cruz"])
    return f'''
    <html>
    <head>
        <style>
            body {{
                background-color: #fff9e6;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }}
            h1 {{
                color: #cc8b00;
                font-size: 50px;
            }}
        </style>
    </head>
    <body>
        <h1>🪙 {resultado} 🪙</h1>
        <p>Recarga la página para lanzar de nuevo</p>
        <a href="/">Volver al inicio</a>
    </body>
    </html>
    '''

app.run(debug=True)
