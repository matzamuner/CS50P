import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Invalid argument number")
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin = response["bpi"]["USD"]["rate_float"]
    amount = bitcoin * n
except requests.RequestException:
    sys.exit("Invalid request")
print(f"${amount:,.4f}")
