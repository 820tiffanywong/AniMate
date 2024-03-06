import os
import psycopg2 as pg


class Connector:
    def __init__(self) -> None:
        self.color = "red"
        try:
            self.conn = pg.connect(
                host="localhost",
                password=os.environ.get("DB_PASSWORD"),
                user="postgres",
                dbname="animate",
                port=5432,
            )
            self.cur = self.conn.cursor()

        except pg.Error as e:
            print("error connecting to database")
        else:
            print("connection successful")
    def get_cursor(self):
        """
        Get a cursor for executing SQL queries.
        """
        return self.cur
    def close(self):
        """
        Close the database connection.
        """
        self.cur.close()
        self.conn.close()
        print("Connection closed.")
    def parse_data(self):
        return self.soup

    def something_else(self):
        anime_names = []

        top_ranks = self.soup.find("table", {"class": "top-ranking-table"})

        animes = top_ranks.findAll("tr", {"class": "ranking-list"})

        for anime in animes:
            title = anime.find("td", {"class": "title"})

            details = title.find("div", {"class": "detail"})

            anime_name = details.find("a").text
            anime_names.append(anime_name)

        return anime_names
