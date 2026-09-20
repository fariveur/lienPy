from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "TON_NOUVEAU_WEBHOOK"

@app.route('/com')
def executer_script():
    remote_addr = request.remote_addr
    forwarded_for = request.headers.get("X-Forwarded-For")
    real_ip = request.headers.get("X-Real-IP")

    message = (
        f"Nouvelle requête reçue\n"
        f"remote_addr : {remote_addr}\n"
        f"X-Forwarded-For : {forwarded_for}\n"
        f"X-Real-IP : {real_ip}"
    )

    requests.post(
        WEBHOOK_URL,
        json={"content": message}
    )

    print(message)

    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)