"""Import des package necessaires"""
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():

    """retourner le message Hello friend !"""
    return 'Hello Friend!'

""" Execution du script"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
