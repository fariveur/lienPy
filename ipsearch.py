from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1550941768952844418/wMfHfY4Q3-OStrMILnaB1XkRjURjERSVoDlP4pKLHooJ8Tk8mSRUmwL-bnW3gIyzCbc0"

@app.route('/com')
def executer_script():
    print("remote_addr :", request.remote_addr)
    print("X-Forwarded-For :", request.headers.get("X-Forwarded-For"))
    print("X-Real-IP :", request.headers.get("X-Real-IP"))

    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)