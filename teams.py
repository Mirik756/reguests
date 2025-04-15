import requests

webhook_url = "https://ssinfis.webhook.office.com/webhookb2/56060621-b2ed-48f4-b41f-011e6c645ece@1543f07f-30f9-407a-9eb5-8a7aec418fff/IncomingWebhook/0731e7d48e984dd3a9a34464816f1e24/481e90f3-38fb-4c8e-bba7-b4c48b8edfd9/V23S_tLZDPiD8hmrz_vySr491LQQrWFbLzzxb4Qt3asug1"
message = {
    "text": "Toto je zpráva z pythonu"
}

# Odeslání zprávy
response = requests.post(webhook_url, json=message)

if response.status_code == 200:
    print("Zpráva byla úspěšně odeslána!")
else:
    print(f"Chyba: {response.status_code}, {response.text}")
