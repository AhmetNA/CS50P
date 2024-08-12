import requests
import sys

def get_data():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()  # JSON verisini sözlüğe çevirir
    return data

def main():
    # missing commmand line argument kontrolü
    try:
        sys.argv[1]
    except IndexError:
        print("Missing command-line argument")
        sys.exit(1)
    # string kontrolü
    try:
        float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    data = get_data()
    # rate değeri bir string olarak geliyor, önce virgülü kaldır
    b_dolar = float(data["bpi"]["USD"]["rate"].replace(",", ""))
    print(b_dolar)
    
    # Kullanıcının girdiği dolar miktarını al
    amount = float(sys.argv[1])    
    print(amount)

    price = amount * b_dolar
    print(f"{price:.2f} USD = {amount} bitcoin")

if __name__ == "__main__":
    main()
