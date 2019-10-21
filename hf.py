"""Import des package necessaires"""
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    """retourner le message Hello friend !"""
    return 'Hello Friend!'
"""executer le script et envoyer le resultat sur le port 5000"""
app.run(host='0.0.0.0', port=5000)
