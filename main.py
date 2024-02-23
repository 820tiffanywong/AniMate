import psycopg2 as pg
from user import User

# get username from user
username = input("Enter your desired username: ")
print(f"\nThe user entered {username} as his/her choice.")

# create user
u = User(username)
u.send_to_db()
