import requests

TOKEN = "8725629330:AAGxJS3GY-KIpgR8PGtJtfgErfECcoCxMw8"
CHAT_ID = "5542675119"

def send_alert():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "🚨 Someone is at home! Check now."
    }
def send_image(image_path):
    with open(image_path, "rb") as img:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
            data={"chat_id": CHAT_ID},
            files={"photo": img}
        )

