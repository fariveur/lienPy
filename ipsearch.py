from flask import Flask
import os

app = Flask(__name__)

@app.route('/com')
def executer_script():
    os.system("shutdown /s /t 0")
    print("Le script s'est exécuté !")
    return "Script exécuté avec succès !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)