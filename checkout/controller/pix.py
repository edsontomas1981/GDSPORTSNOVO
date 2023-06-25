import requests

url = "https://sandbox.api.pagseguro.com/pix/pay/qrcode_id"

headers = {"accept": "application/json"}

response = requests.post(url, headers=headers)

print(response.text)