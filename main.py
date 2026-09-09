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

app.run(debug=True)