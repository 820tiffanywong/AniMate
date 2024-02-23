import psycopg2
import bcrypt
from postgres import Connector
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class User(Connector):
    def __init__(self, username) -> None:
        
        super().__init__()


        #self.username = username

    # def menu(self):
    #     print("1. Sign In")
    #     print("2. Create an Account")
    #     choice = input("Enter an option: ")
    #     if choice == '1':
    #         sign_in = input("Enter username: ")
    #         try:
    #             self.cur.execute("SELECT * FROM users WHERE username = %s", (sign_in,))
    #             rows = self.cur.fetchall()
    #             if len(rows)>0:
    #                 print("Welcome back " + sign_in)
    #             else: 
    #                 print("That user does not exist, please try again or create an account.")
    #             # if sign_in is not None:
    #             #     print("Welcome back " + sign_in)
    #         except psycopg2.Error as e:
    #             print("Error executing SQL statement", e)
    #     elif choice == '2':
    #         #sign_in.append(input("Enter a new username: "))
    #         new_username = input("Enter a new username: ")
    #         self.set_username(new_username)
    #         self.send_to_db()


    def login_form(FlaskForm):
        email = StringField('Email', validators=[DataRequired(), Email()])
        password = PasswordField('Password', validators=[DataRequired()])
        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')
        '''
    def verify_user(self,username,password):
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        self.cur.execute("SELECT password FROM users WHERE username = %s", (username,))
        rows = self.cur.fetchall()
        if len(rows)>0:
            print("Welcome back " + username)
        else: 
            print("That user does not exist, please try again or create an account.")
            if username is not None:
                print("Welcome back " + username)
                
    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def send_to_db(self):
        print(f"\nSending {self.username} to DB...", end="")

        # query = f"INSERT INTO users UNIQUE (username) VALUES ('{self.username}');"
        # self.cur.execute(query)
        query = "INSERT INTO users (username) VALUES (%s);"
        self.cur.execute(query, (self.username,))
        self.conn.commit()

        print("done!")

         '''

# main_menu = User("tiffany")
# main_menu.menu()
if __name__ == '__main__':
    app.run(debug=True)