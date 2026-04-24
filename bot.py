import requests

TOKEN = "8725629330:AAGxJS3GY-KIpgR8PGtJtfgErfECcoCxMw8"
CHAT_ID = "5542675119"

def send_alert():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "Someone is coming to the house, please check"
    }

    response = requests.post(url, data=data)
    print("Message response:", response.text)


def send_image(image_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    with open(image_path, "rb") as img:
        response = requests.post(
            url,
            data={"chat_id": CHAT_ID},
            files={"photo": img}
        )
        print("Image response:", response.text)
        print("TOKEN USED:", TOKEN)