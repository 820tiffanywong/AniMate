import requests
from bs4 import BeautifulSoup as bs
from postgres import Connector
import psycopg2 as pg
from psycopg2.extras import execute_values
import pandas as pd

conn = Connector()
cur = conn.get_cursor()

URL = "https://myanimelist.net/topanime.php"

# print(page.text)


def scrape_data(URL):
    page = requests.get(URL)
    soup = bs(page.content, "html.parser")

    return soup


def parse_data(soup):
    anime_names = []
    top_ranks = soup.find("table", {"class": "top-ranking-table"})
    animes = top_ranks.findAll("tr", {"class": "ranking-list"})
    for anime in animes:
        title = anime.find("td", {"class": "title"})
        details = title.find("div", {"class": "detail"})
        anime_name = details.find("a").text
        anime_names.append(anime_name)

    return anime_names


soup = scrape_data(URL)
anime_data = parse_data(soup)
df = pd.DataFrame({"anime_name": anime_data})

values = [tuple(x) for x in df.to_numpy()]

try:
    execute_values(cur, "INSERT INTO anime VALUES %s", values)
    conn.commit()
    print("data inserted successfully")

except Exception as e:
    print(f"error: {e}")
