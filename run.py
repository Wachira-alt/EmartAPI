from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()

# pipenv install flask flask-sqlalchemy flask-migrate flask-bcrypt flask-cors python-dotenv pyjwt
# pipenv shell
