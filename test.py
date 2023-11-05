import requests

#put token to this data inside the token
token = ""
token = token.strip('"')
def validate_endpoint():
    url ="http://127.0.0.1:8000/profile"
    headers = {
    "Authorization":token,
    "Content-Type": "application/json", }

    response = requests.post(url,headers=headers)
    return response.text


print(validate_endpoint())