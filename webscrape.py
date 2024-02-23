import requests

URL = "https://myanimelist.net/topanime.php"
page = requests.get(URL)

print(page.text)
