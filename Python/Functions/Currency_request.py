import requests

def Rates(ForCurr, Amount, ToCurr):
    response = requests.get("https://api.exchangerate-api.com/v4/latest/" + ForCurr)
    data = response.json()
    rate = data['rates'][ToCurr]
    converted_amount = Amount * rate
    return converted_amount