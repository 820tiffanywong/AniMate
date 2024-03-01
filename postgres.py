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

    def create_user(self, username, fname, lname, password):
        query = f"SELECT 1 FROM users WHERE username = '{username}';"
        self.cur.execute(query)
        current_users = self.cur.fetchall()

        # let user know username is taken
        if len(current_users) > 0:
            print("USERNAME TAKEN")
        else:
            try:
                # Execute the INSERT statement
                self.cur.execute(
                    "INSERT INTO users (username, first_name, last_name, password) VALUES (%s, %s, %s, %s)",
                    (
                        username,
                        fname,
                        lname,
                        password,
                    ),
                )

                username = "twong"
                fname = "tiffany"
                lname = "wong"
                password = "dsnjakdnjska'); DROP TABLE users;"

                # Commit the transaction
                self.conn.commit()
                print("done")

            except Exception as e:
                # Rollback the transaction in case of error
                self.conn.rollback()
                raise e  # Re-raise the exception for handling in the caller

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
